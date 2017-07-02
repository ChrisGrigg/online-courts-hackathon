<template>
  <div>
    <div class="row">
      <div class="col-md-6">
        <h3>Consider Your Options</h3>
      </div>
      <div class="col-md-6 text-right">
        <h5>Step 7 of 7</h5>
      </div>
    </div>
    <br />
    <h5>Case Number: 566778</h5>
    <br />
    <h5>John Doe vs Fred Smith</h5>
    <br />
    <div class="animated fadeIn">
      <div class="card">
        <div class="card-header lead"><i class="icon-note"></i> Options</div>
        <div class="card-block">
          <h5><i class="fa fa-arrow-right mr-1"></i> <u>Proceed</u> <i class="fa fa-info-circle ml-1"></i></h5>
          <h6 class="ml-3">with claim</h6>
          <br />
          <h5><i class="fa fa-arrow-right mr-1"></i> <u>Negotiate</u> <i class="fa fa-info-circle ml-1"></i></h5>
          <h6 class="ml-3">direct with Defendant</h6>
          <br />
          <h5><i class="fa fa-arrow-right mr-1"></i> <u>Blind Bidding</u> <i class="fa fa-info-circle ml-1"></i></h5>
          <h6 class="ml-3">enter the blind bidding process</h6>
          <br />
          <h5><i class="fa fa-arrow-right mr-1"></i> <u>Other Settlement Options</u> <i class="fa fa-info-circle ml-1"></i></h5>
          <h6 class="ml-3">e.g. mediation, un-bundled legal advice</h6>
        </div>
        <div class="card-footer">
          <router-link :to="'/outcome'" class="nav-link d-inline">
            <button class="btn btn-sm btn-primary" type="submit"><i class="fa icon-arrow-left"></i> Back</button>
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
