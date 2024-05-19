<template>
  <div>
    <div class="ImageUpload">
      <div class="Title">
        <p>Upload Image</p>
      </div>
      <el-upload
        class="avatar-uploader"
        :show-file-list="false"
        :on-success="handleSuccess"
        :before-upload="beforeUpload">
        <img v-if="imageUrl" :src="imageUrl" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
      <div class="uploadButton">
        <el-button type="primary" class="mainbutton" @click="UploadConfirm">OK</el-button>
      </div>
    </div>
    <!-- <div class="ResultShow">
      <div class="Title">
        <p>Result</p>
      </div>
      <div class="resultUrlShow">
        <div class="input">
          <el-input
            type="textarea"
            :rows="1"
            placeholder="Result will show here"
            readonly=true
            v-model="textarea">
          </el-input>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ImgaeUpload',
  data(){
    return {
      textarea: '',
      imageUrl: '',
    }
  },
  methods: {
    UploadConfirm(file){
      alert("1321313132")
    },
    handleSuccess(response, file, fileList) {
      // this.imageUrl = URL.createObjectURL(file.raw);
      alert("success")
    },
    beforeUpload(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        // 将文件转化为 base64 编码格式

        reader.readAsDataURL(file);

        reader.onload = () => {

          const imgBase64 = reader.result.split(',')[1]
          console.log(imgBase64)
          // 将处理后的文件通过 ajax 的方式上传到服务器
          this.$axios({
            method: 'post',
            url: 'Upload',
            data: {
              image: imgBase64,
            }
          })
          .then(res => {
            console.log(res);
            resolve(false);
          }).catch(err => {
            reject(err);
          });
        };
      });
    }
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
