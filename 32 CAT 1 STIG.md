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