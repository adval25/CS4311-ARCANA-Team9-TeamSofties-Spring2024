# Security: 32 CAT 1 STIG Vulnerabilities

Justification of CAT 1 STIG Vulnerabilities

VULNERABILITY ID  |           DESCRIPTION          |         MITIGATING REASON                          |
————————————————————————————————————————————————--------------------------------------------------------|
V – 222400        | Validity periods must be       | This is a security measure to prevent the use of   |
                  | verified on all application    | outdated or expired security tokens. This ID would |
                  | messages using WS-Security     | not apply on this project due to the project not   |
                  | or SAML assertions.            | having a need for security tokens &/or passwords.  |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222404        | The application must use       | Specifically, it states that when using the        |
                  | both the NotBefore and         | Conditions element in a SAML assertion, the        |
                  | NotOnOrAfter elements or       | assertion must include either both the NotBefore   |
                  | OneTimeUse element when        | and NotOnOrAfter elements or the Onetime Use       |
                  | using the Conditions element   | element. For this project this would not be        |
                  | in a SAML assertion.           | relevant due that SAML, it’s a secured internet    | 
                  |                                | connection enabler for using relevant Single Sign  |
                  |                                | On on XML, this would not apply.                   |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222612        | The application must not       | To mitigate the risk of overflow attacks, we would |
                  | be vulnerable to overflow      | need to employ secure coding practices and         |
                  | attacks.                       | implement proper input validation, boundary        |
                  |                                | checking, and memory management. Overflow attacks, |
                  |                                | such as buffer overflows, can lead to serious      |
                  |                                | security vulnerabilities, allowing attackers to    | 
                  |                                | overwrite memory and execute arbitrary code.       |
                  |                                | Here are some best practices to prevent overflow   |
                  |                                | attacks:                                           |
                  |                                | -  Input Validation                                |
                  |                                | -  Buffer Size Checks                              |
                  |                                | -  Secure Coding Practices                         |
                  |                                | -  Memory Safety Languages                         |
                  |                                | -  Static Code Analysis                            |
                  |                                | -  Dynamic Anaylsis                                |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222578        | The application must destroy   |                                                    |
                  | the session ID value and/or    |                                                    |
                  | cookie on logoff or browser    |                                                    |
                  | close.                         |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222430        | The application must execute   | In this scenario where the application is used     |
                  | without excessive account      | locally in a browser like Mozilla Firefox and      |
                  | permissions.                   | doesn't connect to the internet, managing session  |
                  |                                | IDs and cookies for local security is still        |
                  |                                | important. Even in a local context, it's crucial   |
                  |                                | to follow secure practices to protect sensitive    | 
                  |                                | information and user sessions.                     |
                  |                                |                                                    |
                  |                                | Here are some considerations that would help to    |
                  |                                | mitigate this STIG:                                |
                  |                                | - Session Management                               |
                  |                                | - Cookie Attributes ('HTTP Only', 'Same Site')     |
                  |                                | - Session Timeout                                  |
                  |                                | - Clear Cookies on browser close                   |
                  |                                | - Secure local storage                             |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222432        | The application must enforce   | ARCANA application does not need user/password     |
                  | the limit of three consecutive | requirements, this STIG is not relevant for this   |
                  | invalid logon attempts by a    | project.                                           |
                  | user during a 15-minute time   |                                                    |
                  | period.                        |                                                    |
——————————————————-—————————————————————————------------------------------------------------------------|
V – 222577        | The application must not expose| It's crucial to implement measures to prevent      |
                  | session IDs                    | session ID exposure, as exposing session IDs can   | 
                  |                                | lead to security vulnerabilities.                  |
                  |                                |                                                    |
                  |                                | Here are some best practices to ensure that        |
                  |                                | session IDs are not exposed:                       |
                  |                                | -  Protect against session fixation                |
                  |                                | -  Session ID rotation                             |
                  |                                | -  Session timeout                                 |
                  |                                | -  Use secure cookies                              |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222609        | The application must not be    | To mitigate input handling vulnerabilities in the  |
                  | subject to input handling      | application, we need to implement robust input     |
                  | vulnerabilities.               | validation, sanitization, and encoding practices.  |
                  |                                |                                                    |
                  |                                | Here are some recommendations to address input     |
                  |                                | handling vulnerabilities:                          |
                  |                                | -  Avoid trusting user input                       |
                  |                                | -  Use parameterized queries                       |
                  |                                | -  File upload security (valid file types and      |
                  |                                |    restrict size)                                  |
                  |                                | -  Error Handling                                  |
                  |                                | -  Input Validation                                |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222608        | The application must not be    | To mitigate XML-oriented attacks in the            |
                  | be vulnerable to XML-oriented  | application, even if it's not connected to the     |
                  | attacks.                       | internet, we can implement the following measures: |
                  |                                | -  Avoid XML External Entity Attacks               |
                  |                                | -  Use a secure XML Parser                         |
                  |                                | -  Input validation for XML Data                   |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222602        | The application must protect   | To mitigate Cross-Site Scripting (XSS)             |
                  | from Cross-Site Scripting (XSS)| vulnerabilities in the locally run application,    |
                  | vulnerabilities.               | follow these best practices:                       |
                  |                                | -  Output encoding                                 |
                  |                                | -  Content Security Policy (CSP)                   |
                  |                                | -  Use frameworks with built-in protection         |
                  |                                |    (e.g. React, Angular, Vue...)                   |
                  |                                | -  Escape Dynamic JavaScript values                |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222601        | The application must not store | To ensure that your application does not store     |
                  | sensitive information in hidden| sensitive information in hidden fields, we can     |
                  | fields.                        | follow these best practices:                       |
                  |                                | -  Avoid Storing Sensitive Data                    |
                  |                                | -  Secure Communication Channels                   |
                  |                                | -  Use local storage                               |
                  |                                | -  Data Masking                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222607        | The application must not be    | Even though MongoDB is a NoSQL database and not    |
                  | vulnerable to SQL Injection.   | susceptible to traditional SQL injection attacks,  |
                  |                                | it's crucial to follow best practices to prevent   |
                  |                                | NoSQL injection or other security vulnerabilities. |
                  |                                |                                                    |
                  |                                | Here are some recommendations to mitigate this:    |
                  |                                | -  Use parameterized queries                       |
                  |                                | -  Sanitize input                                  |
                  |                                | -  Error Handling                                  |
                  |                                | -  Update dependencies                             |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222604        | The application must be        | To protect the application from command injection  |
                  | protected from command         | vulnerabilities, especially in the context of using|
                  | injection.                     | MongoDB, we can follow these best practices to     |
                  |                                |mitigate this:                                      |
                  |                                | -  Use parameterized queries                       |
                  |                                | -  Sanitize input                                  |
                  |                                | -  Error Handling                                  |
                  |                                | -  Update dependencies                             |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222403        | The application must use       | Same as with V-222400 and V- 222404 this would not |
                  | the NotOnOrAfter condition     | apply to this project due to the project not       |
                  | when using the                 | requiring any kind of authentication, SSO or such. |
                  | SubjectConfirmation            |                                                    |
                  | element in a SAML assertion.   |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222585        | The application must fail to a | Ensuring that the application fails to a secure    |
                  | a secure state if system       | state in the event of various failures involves    |
                  | initialization fails, shutdown | implementing robust error handling and recovery    |
                  | fails, or aborts fail.         | mechanisms.                                        |
                  |                                | Here are some guidelines to achieve this:          |
                  |                                | -  Error handling                                  |
                  |                                | -  Graceful initialization                         |
                  |                                | -  Shutdown process                                |
                  |                                | -  Abort handling                                  |
                  |                                | -  Testing Scenarios                               |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222550        | The application, when utilizing| The application does not need any kind of          |
                  | PKI-based authentication, must | authentication/certification use, this would not   |
                  | validate certificates by       | apply for this project.                            |
                  | constructing a certification   |                                                    |
                  | path to an accepted trust      |                                                    |
                  | anchor.                        |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222522        | The application must uniquely  | The application does not need any kind of          |
                  | identify and authenticate      | authentication, but the application to mitigate    |
                  | organizational users           | this is using the user's requirement for their     |
                  | (or processes acting on behalf | initials to recognize who did what.                |
                  | of organizational users).      |                                                    |
                  |                                |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222554        | The application must not       |This application will have no usage for passwords.  |
                  | display passwords/PINs as      |                                                    |
                  | clear text.                    |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222596        | The application must protect   |This application will have no usage for passwords.  |
                  | the confidentiality and        |                                                    |
                  | integrity of transmitted       |                                                    |
                  | information.                   |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222399        | Messages protected with        |N/A; ARCANA will not use WS_Security tokens.        |
                  | WS_Security must use time      |                                                    |
                  | istamps with creation and      |                                                    |
                  | expiration times.              |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222658        | All products must be supported | All products from this application will be         |
                  | by the vendor or the           | supported by the development team and vendor       |
                  | development team.              |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222659        | TThe application must be       | When decommissioned the application will be        |
                  | decommissioned when maintenance| available to terminate any files and storagee.     |
                  | support is no longer available.|                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222551        | The application, when using    |All PKI-Based Authentication will give access to a  |
                  | PKI-based authentication, must |corresponding private key.                          |
                  | enforce authorized access to   |                                                    |
                  | the corresponding private key. |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222620        | Application web servers must be| The application will have no use of the internet.  |
                  | on a separate network segment  |                                                    |
                  | from the application and       |                                                    |
                  | database servers if it is a    |                                                    |
                  | tiered application operating in|                                                    |
                  | the DoD DMZ.                   |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222536        | The application must enforce a | The application will have no use for passwords.    |
                  | minimum 15-character password  |                                                    |
                  | length.                        |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222643        | The application must have the  | The application will give the option to mark       |
                  | capability to mark sensitive/  | sensitive data to specific users.                  |
                  | classified output when required|                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222542        | The application must only store| The application will have no use for passwords.    |
                  | cryptographic representations  |                                                    |
                  | of passwords.                  |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222543        | The application must transmit  | The application will have no use for passwords.    |
                  |only cryptographically-protected|                                                    |
                  | passwords.                     |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222425        | The application must enforce   | This application will give the approved user       |
                  | approved authorizations for    | specific data they are entrusted with.             |
                  | logical access to information  |                                                    |
                  | and system resources in        |                                                    |
                  | accordance with applicable     |                                                    |
                  | access control policies.       |                                                    |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222642        |The application must not contain| The user must give authentication details each     |
                  | embedded authentication data.  | time a user logs in.                               |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222662        |Default passwords must be changed| The application will have no use for passwords.   |
———————————————————————————————————————————-------------------------------------------------------------|
V – 222555        |The application must use         | This application will follow all the guidelines of|
                  |mechanisms meeting the           | Federal Laws, Executive Orders, Policies,         |
                  |requirements of applicable       | Regulations, Stands for the cryptographic module. |
                  |federal laws, Executive Orders,  |                                                   |
                  |directives, policies,regulations,|                                                   |
                  |standards,and guidance for       |                                                   |
                  |authentication to a cryptographic|                                                   |
                  |module.                          |                                                   |
———————————————————————————————————————————-------------------------------------------------------------|