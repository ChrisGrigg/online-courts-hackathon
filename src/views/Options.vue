<template>
  <div>
    <h3>Consider Your Options</h3>
    <br />
    <h5>Case Number: 566778</h5>
    <br />
    <div class="animated fadeIn">
      <div class="card">
        <div class="card-header lead"><i class="icon-note"></i> Options</div>
        <div class="card-block">
          <h3><i class="fa fa-arrow-right mr-1"></i> <u>Proceed</u> <i class="fa fa-info-circle ml-1"></i></h3>
          <h5 class="ml-3">with claim</h5>
          <br />
          <h3><i class="fa fa-arrow-right mr-1"></i> <u>Negotiate</u> <i class="fa fa-info-circle ml-1"></i></h3>
          <h5 class="ml-3">direct with Defendant</h5>
          <br />
          <h3><i class="fa fa-arrow-right mr-1"></i> <u>Blind Bidding</u> <i class="fa fa-info-circle ml-1"></i></h3>
          <h5 class="ml-3">enter the blind bidding process</h5>
          <br />
          <h3><i class="fa fa-arrow-right mr-1"></i> <u>Other Settlement Options</u> <i class="fa fa-info-circle ml-1"></i></h3>
          <h5 class="ml-3">e.g. mediation, un-bundled legal advise</h5>
        </div>
        <!--<div class="card-footer">-->
          <!--<router-link :to="'/outcome'" class="nav-link">-->
            <!--<button id="submitBtn" class="btn btn-sm btn-primary" type="submit">Next <i class="icon-arrow-right"></i></button>-->
          <!--</router-link>-->
        <!--</div>-->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'claim'
}
</script>
