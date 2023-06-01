function main(workbook: ExcelScript.Workbook) {
    let sheet = workbook.getWorksheet('Sheet1')

    let range_product_type = sheet.getRange("D5:D85");
    let product_type = range_product_type.getValues();

    let range_service_type = sheet.getRange("E5:E85");
    let service_type = range_service_type.getValues();

    let range_values = sheet.getRange("F5:H85");

    let rows = range_values.getRowCount();
    let cols = range_values.getColumnCount();

    let sum_k2_licence=0;
    let sum_k2_project = 0;
    let sum_uipath_licence = 0;
    let sum_uipath_project = 0;
    let sum_ranorex_licence = 0;
    let sum_ranorex_project = 0;
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            let actual_product = product_type[row][0]
            let actual_service_type = service_type[row][0]
            let actual_value = range_values.getCell(row, col).getValue()
            if (typeof actual_value === "string") actual_value=0;
           
            if (actual_service_type==="Licensz") {
                switch(actual_product) {
                    case "K2":
                        sum_k2_licence+=actual_value
                        break;
                    case "Teszt automatizáció":
                        sum_ranorex_licence += actual_value
                        break;
                    case "RPA":
                        sum_uipath_licence += actual_value
                        break;
                }
            } else {
                switch (actual_product) {
                    case "K2":
                        sum_k2_project += actual_value
                        break;
                    case "Teszt automatizáció":
                        sum_ranorex_project += actual_value
                        break;
                    case "RPA":
                        sum_uipath_project += actual_value
                        break;
                    }
                }
            }
        }
    sheet.getCell(56, 11).setValue(sum_k2_project)
    sheet.getCell(56, 12).setValue(sum_k2_licence)
    sheet.getCell(60, 11).setValue(sum_ranorex_project)
    sheet.getCell(60, 12).setValue(sum_ranorex_licence)
    sheet.getCell(64, 11).setValue(sum_uipath_project)
    sheet.getCell(64, 12).setValue(sum_uipath_licence)
}