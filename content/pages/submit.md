title: Submit
slug: Submit

<script>

window.onload = (function() {
    for (var i=0; i < 20; i++) {        
        var element = document.getElementById(i);  // For each element in the loop, get the step with that ID #
        if (element === null) {                    // If the element doesn't exist somehow, skip the rest of the for loop.
            continue;
        }
        if (i != 0) {
            element.style.display="none";           // If it's the first element, don't hide it.
        }
        var next = document.getElementById(i+1);    // Get the next element, and if it's not null...
        if (next === null) {
            continue;
        }
        var textareas = element.getElementsByTagName("textarea");   // Find its textarea.
        for (var j = 0; j < textareas.length; j++) {                // There should only be one, this is a bit of a hack.
            var textarea = textareas.item(j);
            textarea.onkeyup = (function(e) {                       // Create an anonymous function which displays the next item when the textarea of the current item is changed.
                return function() {
                    e.style.display="block";
                };
            })(next);
        };
    };
})




</script>

Have you ever made a contribution to an open source project? Tell us about it here. Don't be shy - no contribution is too small. And contributions involving mistakes, confusion, and trying ten different things until something works? Are the best for others to learn from.

We want to hear about all different types of contributions, not just code.  Did you file a bug, design a logo, give user feedback, fix or translate some documentation, or manage an event?  Please tell us your story!

If you're not sure what to write, check out the [featured stories](http://mergestories.com/tags.html#featured-ref).

Please try to give as much detail as you can. Questions marked with an asterisk are required.

<div class="ss-form">
<iframe name="iframe_lfyrwwrj" id="iframe_lfyrwwrj" style="display:none;" onload="if(typeof sent_lfyrwwrj!='undefined'){window.location='http://mergestories.com/pages/submitted.html';}"></iframe>
<form action="https://docs.google.com/forms/d/1RmsXfbOFtPNJ5_LwfS3NcYhFOtq2fseRwef_R222oxM/formResponse"  method="POST" id="ss-form" target="iframe_lfyrwwrj" onsubmit="sent_lfyrwwrj=true"><ol role="list" class="ss-question-list" style="padding-left: 0">
"http://www.mergestories.com/pages/submitted.html"
<div class="form_subhead">The Basics</div>

<div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_2023565106"><div class="ss-q-title">What is your name?
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr">If you&#39;ve submitted a story before, use the same name and readers will be able to see all of your stories together.</div></label>
<input type="text" name="entry.2023565106" value="" class="ss-q-short" id="entry_2023565106" dir="auto" aria-label="What is your name? If you&#39;ve submitted a story before, use the same name and readers will be able to see all of your stories together. " aria-required="true" required="" title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1919080730"><div class="ss-q-title">What is your email address?
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr">This is for the administrators, in case they have questions for you.  It won&#39;t be included in the post.</div></label>
<input type="text" name="entry.1919080730" value="" class="ss-q-short" id="entry_1919080730" dir="auto" aria-label="What is your email address? This is for the administrators, in case they have questions for you.  It won&#39;t be included in the post. " aria-required="true" required="" title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div>

<div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_300556150"><div class="ss-q-title">What project did you make a contribution to?
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<input type="text" name="entry.300556150" value="" class="ss-q-short" id="entry_300556150" dir="auto" aria-label="What project did you make a contribution to?  " aria-required="true" required="" title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1363522345"><div class="ss-q-title">What should we title your story?
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr">If you've got writer's block, try rephrasing the name of the issue you responded to.</div></label>
<input type="text" name="entry.1363522345" value="" class="ss-q-short" id="entry_1363522345" dir="auto" aria-label="What should we title your story?  " aria-required="true" required="" title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="form_subhead">The Story</div>

<div class="ss-q-title">You can add up to 20 steps, but only the first step is required. You can leave the last step blank. Here are some example questions to help you write your story.</div>

<div class="questions">
How did you learn about the project? <br />
How did you find the issue you worked on? Why did you decide to work on it?<br />
Did you talk to anybody who works on the project? <br />
Did you need to set up a development environment? How did you do so?<br />
How did you figure out where to make your changes?<br />
How did you test the changes you made?<br />
How did you contribute your changes back to the project?<br />
What difficulties did you run into, and how did you solve them? Did you turn to any communities or online resources for help?<br />
What did you need to already know to make your contribution, that someone new to open source or software projects in general might not know?<br />
</div>

<div class="ss-form-question errorbox-good" id="0" "role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1389151802"><div class="ss-q-title">The First Step
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1389151802" rows="8" cols="0" class="ss-q-long" id="entry_1389151802" dir="auto" aria-label="Step 1  " aria-required="true" required=""></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="1" "role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_603062675"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.603062675" rows="8" cols="0" class="ss-q-long" id="entry_603062675" dir="auto" aria-label="Step 2  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="2" "role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_178508708"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.178508708" rows="8" cols="0" class="ss-q-long" id="entry_178508708" dir="auto" aria-label="Step 3  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="3" "role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1954301530"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1954301530" rows="8" cols="0" class="ss-q-long" id="entry_1954301530" dir="auto" aria-label="Step 4  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="4" " role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_731379118"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.731379118" rows="8" cols="0" class="ss-q-long" id="entry_731379118" dir="auto" aria-label="Step 5  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="5" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1448384929"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1448384929" rows="8" cols="0" class="ss-q-long" id="entry_1448384929" dir="auto" aria-label="Step 6  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="6" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1224977072"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1224977072" rows="8" cols="0" class="ss-q-long" id="entry_1224977072" dir="auto" aria-label="Step 7  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="7" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_2073139872"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.2073139872" rows="8" cols="0" class="ss-q-long" id="entry_2073139872" dir="auto" aria-label="Step 8  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="8" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1771949325"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1771949325" rows="8" cols="0" class="ss-q-long" id="entry_1771949325" dir="auto" aria-label="Step 9  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="9" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1419921080"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1419921080" rows="8" cols="0" class="ss-q-long" id="entry_1419921080" dir="auto" aria-label="Step 10  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="10" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_2038567721"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.2038567721" rows="8" cols="0" class="ss-q-long" id="entry_2038567721" dir="auto" aria-label="Step 11  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="11" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_65011868"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.65011868" rows="8" cols="0" class="ss-q-long" id="entry_65011868" dir="auto" aria-label="Step 12  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="12" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_122349419"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.122349419" rows="8" cols="0" class="ss-q-long" id="entry_122349419" dir="auto" aria-label="Step 13  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="13" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1515341332"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1515341332" rows="8" cols="0" class="ss-q-long" id="entry_1515341332" dir="auto" aria-label="Step 14  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="14" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_441925640"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.441925640" rows="8" cols="0" class="ss-q-long" id="entry_441925640" dir="auto" aria-label="Step 15  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="15" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_121720266"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.121720266" rows="8" cols="0" class="ss-q-long" id="entry_121720266" dir="auto" aria-label="Step 16  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="16" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_441127551"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.441127551" rows="8" cols="0" class="ss-q-long" id="entry_441127551" dir="auto" aria-label="Step 17  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="17" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1660802530"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1660802530" rows="8" cols="0" class="ss-q-long" id="entry_1660802530" dir="auto" aria-label="Step 18  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="18" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_807514746"><div class="ss-q-title">The Next Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.807514746" rows="8" cols="0" class="ss-q-long" id="entry_807514746" dir="auto" aria-label="Step 19  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="19" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_246933072"><div class="ss-q-title">The Last Step
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr">This is the last step our form will accept. If you want to write more, submit the story and email us with the rest!</div></label>
<textarea name="entry.246933072" rows="8" cols="0" class="ss-q-long" id="entry_246933072" dir="auto" aria-label="Step 20  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="form_subhead">Finishing Up</div>

<div class="ss-form-question errorbox-good" "role="listitem">
<div dir="ltr" class="ss-item  ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_235795032"><div class="ss-q-title">Is your contribution displayed anywhere, for instance in a pull request?  If so, you can put a link to it here.
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<input type="text" name="entry.235795032" value="" class="ss-q-short" id="entry_235795032" dir="auto" aria-label="Is your contribution displayed anywhere, for instance in a pull request?  If so, you can put a link to it here.  " title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_690550334"><div class="ss-q-title">You can suggest some tags for your story, separated by commas.  We can also add tags for you.
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr">View the full list of tags here: <a href="http://www.google.com/url?q=http%3A%2F%2Fmergestories.com%2Ftags.html&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNFvKIQL6f1TiNq0CfVI-1PwjMxk3g" target="_blank">http://mergestories.com/tags.html</a></div></label>
<textarea name="entry.690550334" rows="8" cols="0" class="ss-q-long" id="entry_690550334" dir="auto" aria-label="You can suggest some tags for your story, separated by commas.  We can also add tags for you. View the full list of tags here: http://mergestories.com/tags.html "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div>

By submitting your story, you agree to license it as <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">CC BY-SA 4.0</a>.

<input type="hidden" name="draftResponse" value="[,,&quot;-6022307322665735255&quot;]">
<input type="hidden" name="pageHistory" value="0">
<input type="hidden" name="fbzx" value="-6022307322665735255">
<div class="ss-item ss-navigate"><table id="navigation-table"><tbody><tr><td class="ss-form-entry goog-inline-block" id="navigation-buttons" dir="ltr">
<input type="submit" name="submit" value="Submit" id="ss-submit">
</td></tr></tbody></table></div></ol></form></div>
