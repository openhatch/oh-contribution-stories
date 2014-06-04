title: Submit

<script>

window.onload = (function() {
    for (var i=0; i < 20; i++) {        
        var element = document.getElementById(i);
        if (element === null) {
            continue;
        }
        if (i != 0) {
            element.style.display="none";
        }
        var next = document.getElementById(i+1);
        if (next === null) {
            continue;
        }
        var textareas = element.getElementsByTagName("textarea");
        for (var j = 0; j < textareas.length; j++) {
            var textarea = textareas.item(j);
             console.log(element);
            textarea.onkeyup = (function(e) { 
                return function() {
                    console.log(e);
                    e.style.display="block";
                };
            })(next);
        };
    };
})




</script>

<div class="ss-form"><form action="https://docs.google.com/forms/d/1RmsXfbOFtPNJ5_LwfS3NcYhFOtq2fseRwef_R222oxM/formResponse" method="POST" id="ss-form" target="_self" onsubmit=""><ol role="list" class="ss-question-list" style="padding-left: 0">
<div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_2023565106"><div class="ss-q-title">What is your name?
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr">If you&#39;ve submitted a story before, use the same name and readers will be able to see all of your stories together.</div></label>
<input type="text" name="entry.2023565106" value="" class="ss-q-short" id="entry_2023565106" dir="auto" aria-label="What is your name? If you&#39;ve submitted a story before, use the same name and readers will be able to see all of your stories together. " aria-required="true" required="" title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> <div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_300556150"><div class="ss-q-title">What project did you make a contribution to?
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<input type="text" name="entry.300556150" value="" class="ss-q-short" id="entry_300556150" dir="auto" aria-label="What project did you make a contribution to?  " aria-required="true" required="" title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> <div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1363522345"><div class="ss-q-title">What should we title your story?
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<input type="text" name="entry.1363522345" value="" class="ss-q-short" id="entry_1363522345" dir="auto" aria-label="What should we title your story?  " aria-required="true" required="" title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="0" "role="listitem">
<div dir="ltr" class="ss-item ss-item-required ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1389151802"><div class="ss-q-title">Step 1
<label for="itemView.getDomIdToLabel()" aria-label="(Required field)"></label>
<span class="ss-required-asterisk">*</span></div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1389151802" rows="8" cols="0" class="ss-q-long" id="entry_1389151802" dir="auto" aria-label="Step 1  " aria-required="true" required=""></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="1" "role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_603062675"><div class="ss-q-title">Step 2
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.603062675" rows="8" cols="0" class="ss-q-long" id="entry_603062675" dir="auto" aria-label="Step 2  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="2" "role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_178508708"><div class="ss-q-title">Step 3
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.178508708" rows="8" cols="0" class="ss-q-long" id="entry_178508708" dir="auto" aria-label="Step 3  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="3" "role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_1954301530"><div class="ss-q-title">Step 4
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.1954301530" rows="8" cols="0" class="ss-q-long" id="entry_1954301530" dir="auto" aria-label="Step 4  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" id="4" " role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_731379118"><div class="ss-q-title">Step 5
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<textarea name="entry.731379118" rows="8" cols="0" class="ss-q-long" id="entry_731379118" dir="auto" aria-label="Step 5  "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> 

<div class="ss-form-question errorbox-good" "role="listitem">
<div dir="ltr" class="ss-item  ss-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_235795032"><div class="ss-q-title">Is your contribution displayed anywhere, for instance in a pull request?  If so, you can put a link to it here.
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr"></div></label>
<input type="text" name="entry.235795032" value="" class="ss-q-short" id="entry_235795032" dir="auto" aria-label="Is your contribution displayed anywhere, for instance in a pull request?  If so, you can put a link to it here.  " title="">
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div> <div class="ss-form-question errorbox-good" role="listitem">
<div dir="ltr" class="ss-item  ss-paragraph-text"><div class="ss-form-entry">
<label class="ss-q-item-label" for="entry_690550334"><div class="ss-q-title">You can suggest some tags for your story, separated by commas.  We can also add tags for you.
</div>
<div class="ss-q-help ss-secondary-text" dir="ltr">View the full list of tags here: <a href="http://www.google.com/url?q=http%3A%2F%2Fmergestories.com%2Ftags.html&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNFvKIQL6f1TiNq0CfVI-1PwjMxk3g">http://mergestories.com/tags.html</a></div></label>
<textarea name="entry.690550334" rows="8" cols="0" class="ss-q-long" id="entry_690550334" dir="auto" aria-label="You can suggest some tags for your story, separated by commas.  We can also add tags for you. View the full list of tags here: http://mergestories.com/tags.html "></textarea>
<div class="error-message"></div>
<div class="required-message">This is a required question</div>
</div></div></div>
<input type="hidden" name="draftResponse" value="[,,&quot;-6022307322665735255&quot;]
">
<input type="hidden" name="pageHistory" value="0">


<input type="hidden" name="fbzx" value="-6022307322665735255">

<div class="ss-item ss-navigate"><table id="navigation-table"><tbody><tr><td class="ss-form-entry goog-inline-block" id="navigation-buttons" dir="ltr">
<input type="submit" name="submit" value="Submit" id="ss-submit">
<div class="ss-password-warning ss-secondary-text">Never submit passwords through Google Forms.</div></td>
</tr></tbody></table></div></ol></form></div>
