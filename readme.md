
<div  _ngcontent-ng-c400457649=""  class="markdown">
<h1>Wuzzuf Clone app using Django</h1><p>This is a clone of the Wuzzuf job search website, built using Django. It allows users to search for jobs, create job listings, and apply for jobs.</p><h2>Features</h2><ul>

<li>Search for jobs by keyword, location, and company.</li>

<li>Create job listings with a title, description, location, and salary.</li>

<li>Apply for jobs by submitting your resume and cover letter.</li>

<li>View your job history and applications.</li>

</ul><h2>Requirements</h2><ul>

<li>Python 3.6+</li>

<li>Django 3.0+</li>

<li>MySQL</li>

</ul><h2>Installation</h2><ol>

<li>Clone the repository:</li>

</ol><code-block  _nghost-ng-c3694422351=""  ng-version="0.0.0-PLACEHOLDER"><div  _ngcontent-ng-c3694422351=""  class="code-block ng-star-inserted"><div  _ngcontent-ng-c3694422351=""  class="code-block-wrapper header gmat-subhead-2">Code snippet</div><pre  _ngcontent-ng-c3694422351=""><code  _ngcontent-ng-c3694422351=""  role="text">git clone https://github.com/bard/wuzzuf-clone.git

</code></pre><div  _ngcontent-ng-c3694422351=""  hide-from-message-actions=""  class="code-block-wrapper footer gmat-overline hide-from-message-actions"><div  _ngcontent-ng-c3694422351="">Use code with caution. <a  _ngcontent-ng-c3694422351=""  href="/faq#coding"  target="_blank"  rel="noopener noreferrer"  aria-label="Learn more (opens in a new window)"  class="disclaimer-suffix">Learn more</a></div><button  _ngcontent-ng-c3694422351=""  mat-button-ripple-uninitialized=""  aria-label="Copy code"  mat-icon-button=""  mattooltip="Copy code"  class="mat-mdc-tooltip-trigger copy-button mdc-icon-button mat-mdc-icon-button gmat-mdc-button-with-prefix mat-unthemed mat-mdc-button-base gmat-mdc-button"  jslog="179062;track:generic_click,impression"  mat-button-is-fab="false"><span  class="mat-mdc-button-persistent-ripple mdc-icon-button__ripple"></span><mat-icon  _ngcontent-ng-c3694422351=""  role="img"  class="mat-icon notranslate google-symbols mat-icon-no-color"  aria-hidden="true"  data-mat-icon-type="font">content_copy</mat-icon><span  class="mat-mdc-focus-indicator"></span><span  class="mat-mdc-button-touch-target"></span></button><!----></div></div><!----><!----></code-block><ol  start="2">

<li>Create <span  class="citation-0 underline-recitation">a virtual environment </span><span  class="citation-0 citation-1 underline-recitation">and activate it:</span></li><span  class="citation-0 citation-1 underline-recitation">

</span></ol><span  class="citation-0 citation-1 underline-recitation">

</span><code-block  _nghost-ng-c3694422351=""  ng-version="0.0.0-PLACEHOLDER"><div  _ngcontent-ng-c3694422351=""  class="code-block ng-star-inserted"><div  _ngcontent-ng-c3694422351=""  class="code-block-wrapper header gmat-subhead-2">Code snippet</div><pre  _ngcontent-ng-c3694422351=""><code  _ngcontent-ng-c3694422351=""  role="text"><span  class="citation-0 citation-1 underline-recitation">python3 -m venv venv

source venv/bin/activate

</span></code></pre><div  _ngcontent-ng-c3694422351=""  hide-from-message-actions=""  class="code-block-wrapper footer gmat-overline hide-from-message-actions"><div  _ngcontent-ng-c3694422351="">Use code with caution. <a  _ngcontent-ng-c3694422351=""  href="/faq#coding"  target="_blank"  rel="noopener noreferrer"  aria-label="Learn more (opens in a new window)"  class="disclaimer-suffix">Learn more</a></div><button  _ngcontent-ng-c3694422351=""  mat-button-ripple-uninitialized=""  aria-label="Copy code"  mat-icon-button=""  mattooltip="Copy code"  class="mat-mdc-tooltip-trigger copy-button mdc-icon-button mat-mdc-icon-button gmat-mdc-button-with-prefix mat-unthemed mat-mdc-button-base gmat-mdc-button"  jslog="179062;track:generic_click,impression"  mat-button-is-fab="false"><span  class="mat-mdc-button-persistent-ripple mdc-icon-button__ripple"></span><mat-icon  _ngcontent-ng-c3694422351=""  role="img"  class="mat-icon notranslate google-symbols mat-icon-no-color"  aria-hidden="true"  data-mat-icon-type="font">content_copy</mat-icon><span  class="mat-mdc-focus-indicator"></span><span  class="mat-mdc-button-touch-target"></span></button><!----></div></div><!----><!----></code-block><span  class="citation-0 citation-1 underline-recitation">

</span><ol  start="3"><span  class="citation-0 citation-1 underline-recitation">

</span><li><span  class="citation-0 citation-1 underline-recitation">Install the requirements:</span></li><span  class="citation-0 citation-1 underline-recitation">

</span></ol><span  class="citation-0 citation-1 underline-recitation">

</span><code-block  _nghost-ng-c3694422351=""  ng-version="0.0.0-PLACEHOLDER"><div  _ngcontent-ng-c3694422351=""  class="code-block ng-star-inserted"><div  _ngcontent-ng-c3694422351=""  class="code-block-wrapper header gmat-subhead-2">Code snippet</div><pre  _ngcontent-ng-c3694422351=""><code  _ngcontent-ng-c3694422351=""  role="text"><span  class="citation-0 citation-1 citation-end-0 underline-recitation">pip install -r requirements.txt</span><span  class="citation-1">

</span></code></pre><div  _ngcontent-ng-c3694422351=""  hide-from-message-actions=""  class="code-block-wrapper footer gmat-overline hide-from-message-actions"><div  _ngcontent-ng-c3694422351="">Use code with caution. <a  _ngcontent-ng-c3694422351=""  href="/faq#coding"  target="_blank"  rel="noopener noreferrer"  aria-label="Learn more (opens in a new window)"  class="disclaimer-suffix">Learn more</a></div><button  _ngcontent-ng-c3694422351=""  mat-button-ripple-uninitialized=""  aria-label="Copy code"  mat-icon-button=""  mattooltip="Copy code"  class="mat-mdc-tooltip-trigger copy-button mdc-icon-button mat-mdc-icon-button gmat-mdc-button-with-prefix mat-unthemed mat-mdc-button-base gmat-mdc-button"  jslog="179062;track:generic_click,impression"  mat-button-is-fab="false"><span  class="mat-mdc-button-persistent-ripple mdc-icon-button__ripple"></span><mat-icon  _ngcontent-ng-c3694422351=""  role="img"  class="mat-icon notranslate google-symbols mat-icon-no-color"  aria-hidden="true"  data-mat-icon-type="font">content_copy</mat-icon><span  class="mat-mdc-focus-indicator"></span><span  class="mat-mdc-button-touch-target"></span></button><!----></div></div><!----><!----></code-block><span  class="citation-1">

</span><p><span  class="citation-1 citation-end-1">4.</span> Create a database and migrate the models:</p><code-block  _nghost-ng-c3694422351=""  ng-version="0.0.0-PLACEHOLDER"><div  _ngcontent-ng-c3694422351=""  class="code-block ng-star-inserted"><div  _ngcontent-ng-c3694422351=""  class="code-block-wrapper header gmat-subhead-2">Code snippet</div><pre  _ngcontent-ng-c3694422351=""><code  _ngcontent-ng-c3694422351=""  role="text">python manage.py migrate

</code></pre><div  _ngcontent-ng-c3694422351=""  hide-from-message-actions=""  class="code-block-wrapper footer gmat-overline hide-from-message-actions"><div  _ngcontent-ng-c3694422351="">Use code with caution. <a  _ngcontent-ng-c3694422351=""  href="/faq#coding"  target="_blank"  rel="noopener noreferrer"  aria-label="Learn more (opens in a new window)"  class="disclaimer-suffix">Learn more</a></div><button  _ngcontent-ng-c3694422351=""  mat-button-ripple-uninitialized=""  aria-label="Copy code"  mat-icon-button=""  mattooltip="Copy code"  class="mat-mdc-tooltip-trigger copy-button mdc-icon-button mat-mdc-icon-button gmat-mdc-button-with-prefix mat-unthemed mat-mdc-button-base gmat-mdc-button"  jslog="179062;track:generic_click,impression"  mat-button-is-fab="false"><span  class="mat-mdc-button-persistent-ripple mdc-icon-button__ripple"></span><mat-icon  _ngcontent-ng-c3694422351=""  role="img"  class="mat-icon notranslate google-symbols mat-icon-no-color"  aria-hidden="true"  data-mat-icon-type="font">content_copy</mat-icon><span  class="mat-mdc-focus-indicator"></span><span  class="mat-mdc-button-touch-target"></span></button><!----></div></div><!----><!----></code-block><ol  start="5">

<li>Create a superuser:</li>

</ol><code-block  _nghost-ng-c3694422351=""  ng-version="0.0.0-PLACEHOLDER"><div  _ngcontent-ng-c3694422351=""  class="code-block ng-star-inserted"><div  _ngcontent-ng-c3694422351=""  class="code-block-wrapper header gmat-subhead-2">Code snippet</div><pre  _ngcontent-ng-c3694422351=""><code  _ngcontent-ng-c3694422351=""  role="text">python manage.py createsuperuser

</code></pre><div  _ngcontent-ng-c3694422351=""  hide-from-message-actions=""  class="code-block-wrapper footer gmat-overline hide-from-message-actions"><div  _ngcontent-ng-c3694422351="">Use code with caution. <a  _ngcontent-ng-c3694422351=""  href="/faq#coding"  target="_blank"  rel="noopener noreferrer"  aria-label="Learn more (opens in a new window)"  class="disclaimer-suffix">Learn more</a></div><button  _ngcontent-ng-c3694422351=""  mat-button-ripple-uninitialized=""  aria-label="Copy code"  mat-icon-button=""  mattooltip="Copy code"  class="mat-mdc-tooltip-trigger copy-button mdc-icon-button mat-mdc-icon-button gmat-mdc-button-with-prefix mat-unthemed mat-mdc-button-base gmat-mdc-button"  jslog="179062;track:generic_click,impression"  mat-button-is-fab="false"><span  class="mat-mdc-button-persistent-ripple mdc-icon-button__ripple"></span><mat-icon  _ngcontent-ng-c3694422351=""  role="img"  class="mat-icon notranslate google-symbols mat-icon-no-color"  aria-hidden="true"  data-mat-icon-type="font">content_copy</mat-icon><span  class="mat-mdc-focus-indicator"></span><span  class="mat-mdc-button-touch-target"></span></button><!----></div></div><!----><!----></code-block><ol  start="6">

<li>Start the development server:</li>

</ol><code-block  _nghost-ng-c3694422351=""  ng-version="0.0.0-PLACEHOLDER"><div  _ngcontent-ng-c3694422351=""  class="code-block ng-star-inserted"><div  _ngcontent-ng-c3694422351=""  class="code-block-wrapper header gmat-subhead-2">Code snippet</div><pre  _ngcontent-ng-c3694422351=""><code  _ngcontent-ng-c3694422351=""  role="text">python manage.py runserver

</code></pre><div  _ngcontent-ng-c3694422351=""  hide-from-message-actions=""  class="code-block-wrapper footer gmat-overline hide-from-message-actions"><div  _ngcontent-ng-c3694422351="">Use code with caution. <a  _ngcontent-ng-c3694422351=""  href="/faq#coding"  target="_blank"  rel="noopener noreferrer"  aria-label="Learn more (opens in a new window)"  class="disclaimer-suffix">Learn more</a></div><button  _ngcontent-ng-c3694422351=""  mat-button-ripple-uninitialized=""  aria-label="Copy code"  mat-icon-button=""  mattooltip="Copy code"  class="mat-mdc-tooltip-trigger copy-button mdc-icon-button mat-mdc-icon-button gmat-mdc-button-with-prefix mat-unthemed mat-mdc-button-base gmat-mdc-button"  jslog="179062;track:generic_click,impression"  mat-button-is-fab="false"><span  class="mat-mdc-button-persistent-ripple mdc-icon-button__ripple"></span><mat-icon  _ngcontent-ng-c3694422351=""  role="img"  class="mat-icon notranslate google-symbols mat-icon-no-color"  aria-hidden="true"  data-mat-icon-type="font">content_copy</mat-icon><span  class="mat-mdc-focus-indicator"></span><span  class="mat-mdc-button-touch-target"></span></button><!----></div></div><!----><!----></code-block><p>The app will be available at http://localhost:8000.</p><h2>Usage</h2><p>To use the app, you can log in with your superuser credentials or create a new account. Once you are logged in, you can search for jobs, create job listings, and apply for jobs.</p>
