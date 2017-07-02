<template>
  <div>
    <div class="row">
        <div class="col-md-6">
          <h3>Professional Negligence Claim</h3>
        </div>
        <div class="col-md-6 text-right">
          <h5>Step 5 of 7</h5>
        </div>
    </div>
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
            <label class="col-md-4 form-control-label red">Did you feel the Solicitor was slow in responding to correspondence?</label>
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
            <label class="col-md-4 form-control-label blue">Are there other matters on which you may need to instruct them?</label>
            <div class="col-md-8">
              <form id="mattersInstructForm">
                <label class="radio-inline">
                  <input type="radio" id="mattersInstructYes" name="mattersInstruct" value="Yes" checked="checked">Yes
                </label>
                <label class="radio-inline">
                  <input type="radio" id="mattersInstructNo" name="mattersInstruct" value="No">No
                </label>
              </form>
            </div>
          </div>
        </div>
        <div class="card-footer">
              <button class="btn btn-sm btn-primary" @click="calculate">Next <i class="icon-arrow-right"></i></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueLocalForage from 'vue-localforage'
  const moment = require('moment')
  require('moment/locale/en-gb')
  Vue.use(require('vue-moment'), {
    moment
  })
  Vue.use(VueLocalForage)

  export default {
    name: 'claim',
    methods: {
      calculate (e) {
        e.preventDefault()
        let count = 0
        const list = []
        list.push(document.querySelector('input[name="prevAdv"]:checked').value)
        const years = moment().diff(moment(document.getElementById('dateComplaint').value, 'DD-MM-YYYY'), 'years')
        if (years < 6) {
          list.push('yes')
        }
        list.push(document.querySelector('input[name="apologyGiven"]:checked').value)
        list.push(document.querySelector('input[name="claimantExpertise"]:checked').value)
        list.push(document.querySelector('input[name="mattersInstruct"]:checked').value)
        for (let i = 0; i < list.length; i++) {
          const obj = list[i]
          if (obj.toLowerCase() === 'yes') {
            count++
          }
        }
//        console.log(count)
        this.$setItem('data', count, () => {
          this.$router.push('outcome')
        })
      }
    }
  }
</script>
<style lang="css">
  .red {
    color: #880000;
  }
  .blue {
    color: #00aced;
  }
</style>
