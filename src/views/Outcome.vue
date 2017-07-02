<template>
  <div>
    <div class="row">
      <div class="col-md-6">
        <h3>Consider Your Risks</h3>
      </div>
      <div class="col-md-6 text-right">
        <h5>Step 6 of 7</h5>
      </div>
    </div>
    <br />
    <h5>Case Number: 566778</h5>
    <br />
    <h5>John Doe vs Fred Smith</h5>
    <br />
    <div class="animated fadeIn">
      <div class="card">
        <div class="card-header lead"><i class="icon-note"></i> Outcome</div>
        <div class="card-block">
          <p>A number of factors that may affect the outcome of the claim have been considered. Here is a provisioned indication whether the level of risk is low, moderate or high.</p>
          <h4 id="risk" class="row justify-content-md-center">None</h4>
          <br />
          <div class="row justify-content-md-center">
            <table>
              <tr id="d0Arrow"><td></td></tr>
              <tr id="high" class="d0">
                <td><b>High</b><br />Risk</td>
              </tr>
              <tr id="d1Arrow"><td></td></tr>
              <tr id="medium" class="d1">
                <td><b>Moderate</b><br />Risk</td>
              </tr>
              <tr id="d2Arrow"><td></td></tr>
              <tr id="low" class="d2">
                <td><b>Low</b><br />Risk</td>
              </tr>
            </table>
          </div>
          <br />
          <p><b>Key Reasons:</b></p>
          <ul>
            <li>Received positive professional advice on claim</li>
            <li>Defendant has apologised for error</li>
            <li>Defendant claimed specialist expertise</li>
          </ul>
        </div>
        <div class="card-footer">
          <router-link :to="'/claim'" class="nav-link d-inline">
            <button class="btn btn-sm btn-primary" type="submit"><i class="fa icon-arrow-left"></i> Back</button>
          </router-link>
          <router-link :to="'/options'" class="nav-link d-inline">
            <button class="btn btn-sm btn-primary" type="submit">Next <i class="icon-arrow-right"></i></button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import VueLocalForage from 'vue-localforage'
  Vue.use(VueLocalForage)

  export default {
    name: 'outcome',
    methods: {
      formulate (e) {
        this.$getItem('data', (error, data) => {
          if (error) {
            console.error(error)
          }
          const result = Number(data)
          console.log(result)
          console.log('data: ' + data)
          if (result >= 4) {
            document.getElementById('d2Arrow').style.opacity = '1'
            document.getElementById('low').style.border = 'solid red 5px'
            document.getElementById('low').style.fontSize = '18px'
            document.getElementById('low').style.textDecoration = 'underline'
            document.getElementById('risk').innerHTML = 'Low Risk'
          } else if (result < 4 && result >= 3) {
            document.getElementById('d1Arrow').style.opacity = '1'
            document.getElementById('medium').style.border = 'solid red 5px'
            document.getElementById('medium').style.fontSize = '18px'
            document.getElementById('medium').style.textDecoration = 'underline'
            document.getElementById('risk').innerHTML = 'Moderate Risk'
          } else if (result < 3) {
            document.getElementById('d0Arrow').style.opacity = '1'
            document.getElementById('high').style.border = 'solid red 5px'
            document.getElementById('high').style.textDecoration = 'underline'
            document.getElementById('high').style.fontSize = '18px'
            document.getElementById('risk').innerHTML = 'High Risk'
          }
        })
      }
    },
    mounted: function () {
      this.formulate()
    }
  }
</script>
<style lang="css">

  table {
    width: 50%;
    text-align: center;
    color: white;
  }
  #risk {
    text-decoration: underline;
  }
  .d0 {
    background-color: #880000;
    height: 75px;
  }
  .d1 {
    background-color: orange;
    height: 150px;
  }
  .d2 {
    background-color: #00a67c;
    height: 75px;
  }
  #d0Arrow {
    opacity: 0;
  }
  #d1Arrow {
    opacity: 0;
  }
  #d2Arrow {
    opacity: 0;
  }
  #d0Arrow td:before {
    right: 75%;
    top: 32%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-right-color: #880000;
    border-width: 36px;
    margin-top: -36px;
  }
  #d1Arrow td:before {
    right: 75%;
    top: 49%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-right-color: orange;
    border-width: 36px;
    margin-top: -36px;
  }
  #d2Arrow td:before {
    right: 75%;
    top: 65%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-right-color: #00a67c;
    border-width: 36px;
    margin-top: -36px;
  }
</style>
