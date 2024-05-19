<template>
  <div>
    <div class="ResultShow">
      <div class="Title">
        <p>Delete Image</p>
      </div>
      <div class="resultUrlShow">
        <div class="input">
          <el-input
            type="textarea"
            :rows="1"
            placeholder="Enter the URL of image"
            v-model="textarea">
          </el-input>
        </div>
      </div>
      <div class="uploadButton">
        <el-button type="primary" class="mainbutton" @click="DeleteConfirm">OK</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ImageDelete',
  data() {
    return {
      textarea: '1685513357087.jpg'
    }
  },
  methods: {
    DeleteConfirm: function(){
      alert(this.textarea)
      this.$axios({
        method: 'post',
        url: 'Delete',
        data: {
          s3url: this.textarea,
        }
      })
      .then(res => {
        // console.log(res);
        alert(res.data)
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
    height: 180px;
    margin-left: 30%;
    margin-top: 5%;
    border: 1px solid #000716;
    /* display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center; */
  }
  .uploadButton{
    width: 100%;
    height: 50px;
    margin-top: 30px;
  }
  .resultShow .Title{
    width: 100%;

  }
  .resultUrlShow .input{
    width: 80%;
    margin-left: 10%;

  }
</style>
