---
title: "Bio"
layout: "single"
description: "Biography of Sarah H. Bana for talks, panels, and press."
---

<p class="bio-intro">A ready-to-use biography for talks, panels, introductions, and press. Also available: a <a href="/img/headshot.jpg" download>high-resolution headshot</a>.</p>

<div class="bio-block">
  <button class="bio-copy" data-target="bio-full" type="button">Copy</button>
  <div class="bio-text" id="bio-full">
    <p>Sarah Bana is an Assistant Professor in the Department of Management at the London School of Economics and Political Science (LSE) and a Digital Fellow at the Stanford Digital Economy Lab. Dr. Bana's research explores how new technologies and data reshape the skills and activities of workers and firms. Her research has been published in MIS Quarterly, the Journal of Econometrics, the Journal of Policy Analysis and Management, Sloan Management Review, and proceedings of NeurIPS, and featured by BBC Business Daily, the New York Times, Marketplace, and The Atlantic. Her work has been funded by the Russell Sage Foundation and the Upjohn Institute. Prior to LSE, she was an Assistant Professor of Management Science at Chapman University and a postdoctoral fellow at the Stanford Institute for Human-Centered Artificial Intelligence and MIT's Initiative on the Digital Economy. She received her Ph.D. in Economics from the University of California, Santa Barbara.</p>
  </div>
</div>

<script>
document.querySelectorAll('.bio-copy').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var el = document.getElementById(btn.dataset.target);
    if (!el) return;
    var text = el.innerText.trim();
    navigator.clipboard.writeText(text).then(function () {
      var original = btn.textContent;
      btn.textContent = 'Copied';
      btn.classList.add('copied');
      setTimeout(function () {
        btn.textContent = original;
        btn.classList.remove('copied');
      }, 1500);
    });
  });
});
</script>
