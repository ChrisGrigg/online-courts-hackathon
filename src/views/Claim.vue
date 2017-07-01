<template>
  <div>
    <h3>Professional Negligence Claim</h3>
    <br />
    <h5>Case Number: 566778</h5>
    <br />
    <h5>John Doe vs Fred Smith</h5>
    <br />
    <div class="animated fadeIn">
      <div class="card">
        <div class="card-header lead"><i class="icon-note"></i> Questions</div>
        <div class="card-block">
          <!--<p>Answer the following questions and receive a prediction on the outcome of your claim.</p>-->
          <!--<p>This prediction uses statistical analysis with a sprinkle of machine learning to get red hot accuracy.</p>-->

          <div class="form-group row">
            <label class="col-md-4 form-control-label">Have you received positive professional advice on the claim?</label>
            <div class="col-md-8">
              <form id="prevAdvForm">
                <label class="radio-inline">
                  <input type="radio" id="prevAdvYes" name="prevAdv" value="Yes" checked="checked">Yes
                </label>
                <label class="radio-inline">
                  <input type="radio" id="prevAdvNo" name="prevAdv" value="No">No
                </label>
              </form>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-md-4 form-control-label">State the date when the matters complained of occurred</label>
            <div class="col-md-8">
              <input class="form-control" type="date" value="2011-08-19" id="dateComplaint">
            </div>
          </div>
          <div class="form-group row">
            <label class="col-md-4 form-control-label">Has the defendant apologised for the error?</label>
            <div class="col-md-8">
              <form id="apologyGivenForm">
                <label class="radio-inline">
                  <input type="radio" id="apologyGivenYes" name="apologyGiven" value="Yes" checked="checked">Yes
                </label>
                <label class="radio-inline">
                  <input type="radio" id="apologyGivenNo" name="apologyGiven" value="No">No
                </label>
              </form>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-md-4 form-control-label">Did you feel the Solicitor was slow in responding to correspondence?</label>
            <div class="col-md-8">
              <form id="claimantExpertiseForm">
                <label class="radio-inline">
                  <input type="radio" id="claimantExpertiseYes" name="claimantExpertise" value="Yes" checked="checked">Yes
                </label>
                <label class="radio-inline">
                  <input type="radio" id="claimantExpertiseNo" name="claimantExpertise" value="No">No
                </label>
              </form>
            </div>
          </div>
          <div class="form-group row">
            <label class="col-md-4 form-control-label">Are there other matters on which you may need to instruct them?</label>
            <div class="col-md-8">
              <form id="claimantExpertiseForm">
                <label class="radio-inline">
                  <input type="radio" id="claimantExpertiseYes" name="claimantExpertise" value="Yes" checked="checked">Yes
                </label>
                <label class="radio-inline">
                  <input type="radio" id="claimantExpertiseNo" name="claimantExpertise" value="No">No
                </label>
              </form>
            </div>
          </div>
        </div>
        <div class="card-footer">
          <router-link :to="'/outcome'" class="nav-link">
            <button id="submitBtn" class="btn btn-sm btn-primary" type="submit">Next <i class="icon-arrow-right"></i></button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'claim'
}
</script>
