<template>
  <div>
    <div class="home">
      <div class="header">
        <el-button type="primary" class="sign up">
          Sign In
        </el-button>
        <el-button type="primary" class="sign up" @click="GoSignUpPage">
          Sign Up
        </el-button>
        <el-button type="primary" class="sign up">
          Sign Out
        </el-button>
      </div>
    </div>
    <div class="functionChoose">
      <el-button type="primary" class="functionbutton" @click="ToUploadImage">Upload Image</el-button>
      <el-button type="primary" class="functionbutton" @click="ToDeleteImage">Delete Image</el-button>
      <el-button type="primary" class="functionbutton" @click="ToFindwithTag">Find With Tag</el-button>
      <el-button type="primary" class="functionbutton" @click="ToFindwithImage">Find With Image</el-button>
      <el-button type="primary" class="functionbutton" @click="ToAddTag">Add Tag</el-button>
      <el-button type="primary" class="functionbutton" @click="ToDeleteTag">Delete Tag</el-button>
    </div>
    <image-upload v-show="show1"></image-upload>
    <image-delete v-show="show2"></image-delete>
    <findwith-tag v-show="show3"></findwith-tag>
    <findwith-image v-show="show4"></findwith-image>
    <add-tag v-show="show5"></add-tag>
    <delete-tag v-show="show6"></delete-tag>
  </div>
</template>

<script>
  import ImageUpload from './component/imageUpload.vue'
  import ImageDelete from './component/imageDelete.vue'
  import FindwithTag from './component/findwithTag.vue'
  import FindwithImage from './component/findwithImage.vue'
  import AddTag from './component/addTag.vue'
  import DeleteTag from './component/deleteTag.vue'

export default {
  name: 'home',
  data() {
    return {
      imageUrl: '',
      show1: true,
      show2: false,
      show3: false,
      show4: false,
      show5: false,
      show6: false,
    };
  },
  methods: {
    GoSignUpPage: function(){
      this.$router.push('/register')
    },
    ToUploadImage: function(){
      this.show1 = true; this.show2 = false; this.show3 = false; this.show4 = false; this.show5 = false; this.show6 = false
    },
    ToDeleteImage: function(){
      this.show1 = false; this.show2 = true; this.show3 = false; this.show4 = false; this.show5 = false; this.show6 = false
    },
    ToFindwithTag: function(){
      this.show1 = false; this.show2 = false; this.show3 = true; this.show4 = false; this.show5 = false; this.show6 = false
    },
    ToFindwithImage: function(){
      this.show1 = false; this.show2 = false; this.show3 = false; this.show4 = true; this.show5 = false; this.show6 = false
    },
    ToAddTag: function(){
      this.show1 = false; this.show2 = false; this.show3 = false; this.show4 = false; this.show5 = true; this.show6 = false
    },
    ToDeleteTag: function(){
      this.show1 = false; this.show2 = false; this.show3 = false; this.show4 = false; this.show5 = false; this.show6 = true
    }

  },
  components:{
    ImageUpload: ImageUpload,
    ImageDelete: ImageDelete,
    FindwithTag: FindwithTag,
    FindwithImage : FindwithImage,
    AddTag: AddTag,
    DeleteTag: DeleteTag,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .header{
    width: 100%;
    height: 60px;
    background-color: #232f3e;
    display: flex;
    align-items: center;
    justify-content: right;
  }
  .sign{
    width: 5%;
    height: 60%;
    background-color: #f90;
    margin-right: 10px;
    border-radius: 18px;
    font-weight: 700;
    color: #000716;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 0px;
  }
  .in{
    color: blueviolet;
  }
  .functionChoose{
    width: 100%;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 50px;
    margin-bottom: -10px;
  }
</style>
