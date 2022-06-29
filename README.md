# Python TranslateTool
**Python translate file format tool.**  <br/>
**You can use this script to translate all python file to a uniform indent format by space or by tab. <br/>**
<br/>
**Python add source code license tool, very convenient for you to add open source license!** <br/>

# How to use cleanup format tool?
**python3 TranslateTool.py {fileName}  {space or tab}**       <br/>
parameter tab means replace 4 space by tab                <br/>
space means replace tab by 4 space                         <br/>
**example:**                                              <br/>
  **python3 TranslateTool.py cleanup  <fileType|fileName>**    // to clear extra space or tab <br/>
  **python3 TranslateTool.py testdata space**                  // which means replace all 4 space each line by tab  <br/>
  **python3 TranslateTool.py -all {space|tab} {fileType}**          // which means all .c file replace all 4 space each line by tab, fileType means .c .cpp .go .py etc... <br/>

# How to use add File License tool?
**usage:** <br/>
**python3 AddLicenseTool.py -h** <br/>
**python3 AddLicenseTool.py {fileName} {licenseFileName}**    // Add license header by your license file <br/>

# TODO
Later I will support more file types.
