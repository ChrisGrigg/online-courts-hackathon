<template>
  <div>
    <h3>Consider Your Risks</h3>
    <br />
    <h5>Case Number: 566778</h5>
    <br />
    <div class="row">
      <h5 class="col-md-4 text-center">John Doe</h5>
      <h5 class="col-md-4 text-center">vs</h5>
      <h5 class="col-md-4 text-center">Fred Smith</h5>
    </div>
    <br />
    <div class="animated fadeIn">
      <div class="card">
        <div class="card-header lead"><i class="icon-note"></i> Outcome</div>
        <div class="card-block">
          <p>A number of factors that may affect the outcome of the claim have been considered. Here is a provisioned indication whether the level of risk is low, moderate or high.</p>
          <div class="row justify-content-md-center">
              <img src="static/img/Traffic_light_03.png" alt="Traffic light indicator">
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
