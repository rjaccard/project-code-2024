# Case Studies 

After discussing secure software development, security policies, software testing strategies, mitigations, and attack vectors, we will focus on several case studies that apply or refine the software security process. Software security is not static but must be adapted to a given situation to maximize protection.

We will evaluate two case studies: web security and mobile security. For web security, the attacker model includes both the server providing the web services and the browser or client running the web application. For mobile security, the central control over the market place allows the provider to thoroughly test apps before they are installed.

## 7.1 Web Security

Web security is a broad topic that would deserve its own book due to the many aspects that need to be secured. In this Section, we will look at three broad aspects of web security: protecting the server, protecting the interaction between server and client, and protecting the web browser. Web servers (and browsers) are long running software applications that are exposed to adversaries as they serve external requests. Generally, software daemons are long running services that serve external requests. Daemons often run in the background to provide functionalities to a system or, over the network, to multiple concurrent clients.

A web server, mail server, or a DNS server are examples of daemons.

## 7.1.1 Protecting Long Running Services

After initialization, daemons run for a long time, from days to weeks, to months without being restarted. Several mitigations such as ASLR or stack integrity rely on probabilistic guarantees where information is hidden from an adversary. Servers often run multiple threads that are restarted after handling a certain number of requests. Erring towards availability over security, crashing threads are restarted. An adversary can therefore leverage information leaks to recover secrets in a processes address space such as the memory layout to bypass ASLR or stack canary values to bypass stack canaries. Daemons are complex as they serve requests in parallel through multiple threads. As such they are optimized for performance and leverage, e.g., distributed caches to reduce the per request cost, and they offer broad functionalities for different clients.

This large complexity increases the risk for bugs. Complexity results in more code and code size correlates with the number of bugs in a given application.

As they are connected to the network, daemons are often exposed to the internet where they can be attacked from any remote location.

The internet and the web are open platforms, allowing anyone to connect and request services. This increases the risk that someone will launch a remote attack. Especially web servers provide functionality openly to users without requiring authentication or identification of the user.

A reasonable approach to reduce the attack surface of daemons is to break them into smaller components. These components then serve as fault compartments and fail independently. The overall idea is that when one component fails, others continue to function without opening security holes. Components communicate through well-defined APIs and, if one component is buggy, adversaries are restricted to the capabilities of the buggy component and must interact only with the privileges of that component. Without compartmentalization, the adversary would gain all privileges required by the service instead of a small subset.

A good example for compartmentalization are mail servers.

Mail servers have a plethora of tasks: sending and receiving data from the network on a privileged port, parsing the mail protocol, managing a pool of received and unsent messages, providing access to stored messages for each user. The classic approach (implemented in sendmail) is to provide a single binary that executes all theses tasks. Due to the large amount of privileges required (full access to the file system, access to the network), the component runs as root with full administrator privileges. As the mail server accepts connections from the network, this results in a large attack surface and a prominent target that has been attacked frequently.

The modern approach (implemented in qmail) breaks the mailserver into a set of components that communicate with each other. Separate modules run as separate user IDs to provide isolation. Each ID has only limited access to a subset of resources, enforcing least privilege. Only two components run as root and suid root respectively. The central component qmail-queue is privileged to run as qmailq user on behalf of arbitrary users. This small component allows anyone to register new mail in the mail queue. The qmail-send component received messages from the queue and either delivers them to qmail-rspawn to deliver them remotely or qmail-lspawn to deliver them locally. The qmail-lspawn component runs as root as it spawns a local delivery process with the correct target userid (of the receiving user). The qmail-local process runs on behalf of the target user and executes local mail filtering, spam filtering, and user-specific scripts. Note that this enables the mail server to allow customizable per-user filtering without exposing any attack surface. For incoming email, either an unprivileged network server listens for incoming messages and executes spam filtering and other tests or a local mail injection scripts passes messages to the qmail queue. Figure 7.1 gives an overview of the qmail system.

## 7.1.2 Browser Security

Protecting a browser is similar to protecting a daemon. Browsers are long running processes (when have you last restarted your browser?). Through tabs, browsers run multiple contexts at the same time, often 10s or 100s of tabs are open concurrently and each tab must be isolated from each other.

A browser enables an interesting attacker model as the adversary can run JavaScript code on a victim's computer. The JavaScript compiler therefore needs to ensure that no information leaks from the process into the JavaScript sandbox. Similar to mail servers discussed in the previous section, browsers can be implemented as single process with shared state/heap and multiple threads (Firefox) or broken into different processes (Chromium).

For Chromium, each tab corresponds to an individual process. The complex and error prone task of parsing and rendering html is compartmentalized in an unprotected process with limited interaction capabilities to outside processes.

This sandbox ensures that outside interactions are limited and restricted to a well-known API. Browsers are thoroughly tested to ensure that they follow strict security guidelines.

## 7.1.3 Command Injection

The Unix philosophy is to leverage the combination of simple tools to achieve complex results. Many servers therefore leverage the int system(char *cmd) command to start new processes to execute simple Unix commands. Potentially tainted data from forms or user input is passed to these scripts or programs as parameters. The system command is an example where both code and data are mixed: both the command that is executed and the arguments are passed in a single string. Dynamic web pages, for example, execute code on the server.

This allows the web server to add rich content from other sources such as databases or files, providing dynamic content to the user. The dynamic web page executes as a script on the server side to collect information, build up the page, and send it back to the user. A content management system may load content from the database, a set of files, and other remote parties, then intersect the information with the site template, add navigation modules, and send it back to the user.

```
<html><head><title>Display a **file**</title></head>
<body>
<? **echo system**("cat ".$_GET['file']); ?>
</body></html>
```

The PHP script above leverages the simple cat utility to return the contents of a user supplied file back to the user. Unfortunately, system executes a full shell, resulting in powerful command injection vulnerabilities. The arguments to system are the string cat concatenated with the user-supplied value in the parameter file, e.g., through http://web.site/?file=user. For example ; allows chaining two commands such as http://web.site/?file=user%3Bcat%20%2fetc%2fpasswd to leak /etc/passwd. Simply blocking ; is not enough, the user supplied data in file is untrusted and must be pruned either through validation (comparing against a set of allowed values) or escaping where the user-supplied values are clearly marked as string, e.g., resulting in system("cat 'file; cat
/etc/passwd'") which would result in a file not found error.

Note that you should not write your own escape functions, each web framework has their own escape functions that allow for different contexts.

Even better, instead of leveraging system, simply open and read the file instead of launching a set of sub processes. Command injection attacks are enabled through the fact that code and data share a communication channel. The system function expects a single string for both the command and the argument. A better system function would expect the command as first argument and all the arguments as the second argument. This is similar to code injection where, e.g., the stack can contain both code and data, allowing a buffer overflow to overwrite the instruction pointer to return to the stack.

## 7.1.4 Sql Injection

SQL injection is similar to command injection: an SQL query contains both code and data. For example: $sql = "SELECT
* FROM users WHERE email='" . $_GET['email'] . "'
AND pass='" . $_GET['pwd'] . ';" creates an SQL query string with user input that can be sent to a database. Unfortunately, the user-supplied parameters are not escaped.

An adversary may inject ' characters to escape queries and inject commands.

For example, an adversary may enter asdf' OR 1=1 -- in the password field to bypass the password check.

To mitigate SQL
injection, we apply the same idea:
user-supplied arguments have to be validated or escaped.

Alternatively, the control and data channel should be separated by using prepared SQL statements, similar to how printf defines a format string and with arguments that are then filled in:
sql("SELECT * FROM users WHERE email=\$1
AND pwd=\$2", email, pwd).

## 7.1.5 Cross Site Scripting (Xss)

Cross Site Scripting (or XSS) exploits trust user has in a web site. XSS enables an adversary to inject and execute JavaScript
(or other content) in the context of another web page. For example, malicious JavaScript code may be injected into a banking web page to execute on behalf of a user that is logged into her bank account. This allows the adversary to extract username and password or to issue counterfeit transactions. There are three different kinds of XSS: persistent/stored, reflected, and client-side XSS.

Persistent XSS modifies data stored on the server to include JavaScript code. The adversary interacts with the web application, storing the code on the server side. When the user interacts with the web application, the server responds with a page that includes the attacker-supplied code. An example of persistent XSS is a simple chat application where the adversary includes <script>alert('Hi there');</script> in the chat message. This message is stored in a database on the server.

When the message is sent to the user, the JavaScript code is executed on behalf of the user's browser in the user's session. Persistent XSS is enabled through a lack of input sanitization on the server side. Common locations of such errors are feedback forms, blog comments, or even product meta data (you do not have to see the response to execute it). In this scenario, the user only has to visit the compromised website.

Reflected XSS encodes the information as part of the request which is then reflected through the server back to the user.

Instead of storing the JavaScript code on the server side, it is encoded as part of the link that the user clicks on. A web interface may return the query as part of the results, e.g.,
"Your search for 'query' returned 23 results.". If the query is not sanitized, then JavaScript code will be executed on the user side. The code is encoded as part of the link and the user is tricked to click on the prepared link. The bug for this type of XSS is on the server side as well.

Client-side XSS targets lack of sanitization on the client side.

Large web applications contain a lot of JavaScript code that also parses input data from, e.g., AJAX/JSON requests or even input that is passed through the server. This JavaScript code may contain bugs and missing sanitization that allows the adversary to execute injected JavaScript in the context of the web application as the user. Similarly to reflected XSS, the user must follow a compromised link. The server does not embed the JavaScript code into the page through server-side processing but the user-side JavaScript parses the parameters and misses the injected code. The bug is on the client side, in the server-provided JavaScript.

## 7.1.6 Cross Site Request Forgery (Xsrf)

Cross Site Request Forgery (XSRF) exploits trust a web app has in user's browser. Given that a user is logged into a web page, certain links may trigger state changes on behalf of that user. For example, the URL "http://web.site/?post=Hello" may create a new public post on a bulletin board on behalf of the user with the content 'Hello'. An adversary that knows the URL pattern can construct URLs that trigger actions on behalf of a user if they click on it. Instead of creating a public post, the action could be a money transfer from the user's bank account to the attacker.

## 7.2 Mobile Security

Smart mobile devices have become ubiquitous: from smart phones to tablets and smart watches, they all run a form of mobile operating system that allows installation of apps from a central market. Android is one of two dominant ecosystems that cover the mobile platform. A hard challenge for Android is the large amount of different devices from different hardware vendors that is customized through different carriers. This results in a slow update process as all these different devices are hard to maintain and update.

The Android ecosystem enforces strict security policies that reduce the risk of running malicious apps. The basic Android system is configured to reduce the risk of software vulnerabilities by using a secure basic system configuration combined with strong mitigations. Individual apps are isolated from each other. Applications are installed from a central market. Each app in the market is vetted and tested through static and dynamic analysis to detect malicious code.

## 7.2.1 Android System Security

Android is built on Linux and therefore follows a basic Unix system design. Instead of running multiple applications under a single user id, each application is associated its own "user". Under the Unix design, each user has a home directory and associated files. Each application started by the user can access all the files of that user. Under Android, each app runs as its own user id and is therefore restricted to access only the files of that user. Interaction between apps is controlled through intents and a well-defined API.

The Android system leverages a hardened Linux kernel to protect against attacks from malicious apps. Apps are isolated from each other through the user id interface and the kernel is configured to reduce side channels through, e.g., the "/proc" interface. The filesystem follows a stringent set of permissions to reduce exposure and an SELinux policy enforces access control policies on processes. To protect against cold boot attacks or hardware attacks, Android leverages full filesystem encryption that is seeded from the user password. Services and daemons in user space leverage stack canaries, integer overflow mitigation, double free protection through the memory allocator, fortify source, DEP, ASLR, PIE, relro (mapping relocations as readonly after resolving them), and immediate binding (mapping the procedure linkage table as read-only after forcefully resolving all inter-module links). Each Android update includes security updates, patches, updates to the toolchain and tighter security defaults. Overall, Android follows a secure system default configuration and restricts interactions between apps and the system.

## 7.2.2 Android Market

Linux distributions like Debian or Ubuntu have long provided a central market of curated applications. Developers provide their applications and package maintainers make sure that they fit well into the existing ecosystem of a distribution. Package maintainers are responsible to backport patches and ensure a smooth operation and integration between all the different applications that make up a distribution.

The Android mobile app market is similar and provides a central place where users can search for and install new apps. Developers sign apps (and their required permissions) and upload the apps to the market.

Google can then vet and check apps before they are provided to individual users. Each application is tested for malicious code or behavior. Entrance to the market is regulated. Each developer must pay an entrance fee to upload apps. This entrance fee allows Google to offset the cost of the vetting process. If a malicious app is detected, all apps of a user can be blocked. This limits the amount of malicious code a user can upload and increases the risks for attackers that all their apps are blocked.

Whenever an app is updated and uploaded to the market, it is distributed to all devices that have it installed.

This automatic update process minimizes the risk of exposure as the new version is pushed to the clients quickly.

## 7.2.3 Permission Model

The app permission model restricts what devices an app has access to. The complex permission system allows a fine-grained configuration on a per-app basis on access to Camera, location information, Bluetooth services, telephony, SMS/MMS functionality, and network/data connections. Without privileges, an app is restricted to computation, graphics, and basic system access.

The user can select if they accept the permissions required by the app and if it matches the expected behavior. This model empowers the user to make security decisions. Whether the user is able to make informed decisions about security matters remains questionable. The user already searched for an app and is trying to install it. What are the chances that they will be negatively influenced through an over-privileged app? A better system to manage privileges remains to be found and is an active research area.