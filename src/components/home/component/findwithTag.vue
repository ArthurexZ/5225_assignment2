<template>
  <div>
    <div class="ImageUpload">
      <div class="Title">
        <p>Find With Tag</p>
      </div>
      <!-- <div class="enterTag">
        <el-input v-model="inputTag" placeholder="please enter tag" class="in"></el-input>
      </div> -->
<!-- 在这里展示想要查找的tag -->
      <div class="showTag">
        <el-tag
          class="Tagsize"
          :key="tag"
          v-for="tag in dynamicTags"
          closable
          :disable-transitions="false"
          @close="handleClose(tag)">
          {{tag}}

        </el-tag>
        <el-input
          class="input-new-tag"
          v-if="inputVisible"
          v-model="inputValue"
          ref="saveTagInput"
          size="small"
          @keyup.enter.native="handleInputConfirm"
          @blur="handleInputConfirm"
        >
        </el-input>
        <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>

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
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FindwithTag',
  data() {
    return {
      inputTag: '',
      dynamicTags: ['cat'],
      inputVisible: false,
      inputValue: '',
      textarea: '',
    }
  },
  methods: {
    UploadConfirm: function(){
      alert(this.dynamicTags)
      this.$axios({
        method: 'put',
        url: 'TagFind',
        data: {
          tags: this.dynamicTags
        }
      })
      .then(res => {
        console.log(res.data.urls);
        this.textarea = res.data.urls
        resolve(false);
      }).catch(err => {
        reject(err);
      });
    },
    TagEnterConfirm: function(){
      alert(this.inputTag)

      this.inputTag = ''
    },
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
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
  .showTag{
    width: 100%;
  }
  .Tagsize{
    font-size: 15px;
    font-weight: 700;
  }
  .el-tag + .el-tag {
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    margin-left: 10px;
    vertical-align: bottom;
    font-size: 15px;
    font-weight: 700;
  }
  .Title{
      width: 100%;
      height: 50px;
      margin-top: 10px;
      font-weight: 700;
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
