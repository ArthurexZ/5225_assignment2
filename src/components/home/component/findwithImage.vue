<template>
  <div>
    <div class="ImageUpload">
      <div class="Title">
        <p>Find With Image</p>
      </div>
        <div class="input">
          <el-input
            type="textarea"
            :rows="1"
            placeholder="Enter The URL"
            v-model="InputTextarea">
          </el-input>
        </div>
      <div class="uploadButton">
        <el-button type="primary" class="mainbutton" @click="UploadConfirm">Find</el-button>
      </div>
    </div>
    <div class="ResultShow">
      <div class="Title">
        <p>Result</p>
      </div>
      <div class="resultUrlShow">
        <div class="output">
          <el-input
            type="textarea"
            :rows="1"
            placeholder="Result will show here"
            readonly=true
            v-model="OutputTextarea">
          </el-input>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FindwithImage',
  data(){
    return {
      InputTextarea: '1685513357087.jpg',
      OutputTextarea: '',
    }
  },
  methods: {
    UploadConfirm: function(){
      alert(this.InputTextarea)
      this.$axios({
        method: 'post',
        url: 'ImageFind',
        data: {
          s3url: this.InputTextarea,
        }
      })
      .then(res => {
        console.log(res);
        this.OutputTextarea = res.data.targetTags
        resolve(false);
      }).catch(err => {
        reject(err);
      });
    },
  }
}
</script>

<style scoped>
  .ImageUpload{
    margin-top: 50px;
    height: 350px;
    width: 40%;
    margin-left: 30%;
    border: 1px solid #000716;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    justify-content: center;
  }
  .Title{
      width: 100%;
      height: 50px;
      margin-top: 10px;
      font-weight: 700;
  }
  .input{
    width: 80%;
  }
  .avatar-uploader .el-upload {
      border: 1px dashed #d9d9d9;
      border-radius: 6px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      margin-top: -1  0px;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
  .ResultShow{
    width: 40%;
    height: 150px;
    margin-top: 5%;
    margin-left: 30%;
    border: 1px solid #000716;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
  }
  .resultUrlShow{
    width: 80%;
    margin-top: -20px;
  }
  .uploadButton{
    width: 100%;
    height: 50px;
  }
  .resultShow .Title{
    width: 100%;

  }
  .resultUrlShow .input{
    width: 80%;
    margin-left: 10%;
  }
</style>
