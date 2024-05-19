<template>
  <div>
    <div class="mainbody">
      <div class="bodycenter">
        <div class="mail inbox">
          <div class="inputTitle">
            <p>Email</p>
          </div>
          <el-input v-model="inputMail" placeholder="please enter your Email address" class="in"></el-input>
        </div>
        <div class="FamilyName inbox">
          <div class="inputTitle">
            <p>Family Name</p>
          </div>
          <el-input v-model="inputFamily" placeholder="please enter your family name" class="in"></el-input>
        </div>
        <div class="GivenName inbox">
          <div class="inputTitle">
            <p>Given Name</p>
          </div>
          <el-input v-model="inputGiven" placeholder="please enter your given name" class="in"></el-input>
        </div>
        <div class="Password inbox">
          <div class="inputTitle">
            <p>Password</p>
          </div>
          <el-input v-model="inputPassword" placeholder="please enter your password" class="in" show-password></el-input>
        </div>
      </div>

    </div>
    <el-button type="primary" class="mainbutton" @click="RegisterConfirm">OK</el-button>
  </div>
</template>

<script>
  export default{
    name: 'Mainbody',
    data() {
        return {
          inputMail: '',
          inputFamily: '',
          inputGiven: '',
          inputPassword: '',
        }
      },
    methods:{
      RegisterConfirm: function(){
        alert("test")
      }
    }
  }

</script>

<style>
  .mainbody{
    display: flex;
    align-items: center;
    justify-content: center;
    padding-top: 150px;
  }
  .bodycenter{
    width: 16%;
    height: 500px;
    background-color: #ffffff;
    border: #ddd;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }
  .inputTitle{
    width: 60%;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-left: 0%;
  }
  .inbox{
    width: 100%;
    height: 70px;
  }
  .in{
    width: 414px;
    height: 54px;
  }
  .mainbutton{
    margin-left: 0%;
    background-color: #f90;
    border: 0px;
  }
</style>
