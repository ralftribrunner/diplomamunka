function main(workbook: ExcelScript.Workbook) {
    let sheet = workbook.getWorksheet('Marketing dataset')

    let accIncome2020 = sheet.getRange("D2:D38").getValues();
    let accIncome2021 = sheet.getRange("F2:F38").getValues();
    let measurement = sheet.getRange("H2:H38").getValues();
    let income2020 = sheet.getRange("E2:E38")
    let income2021 = sheet.getRange("G2:G38")

    let rows = income2020.getRowCount()

    for (let row = 0; row < rows; row++) {

        switch (measurement[row][0]) {
            case "mEUR":
                sheet.getCell(row + 1, 4).setValue(Number(accIncome2020[row][0]) * 1000000 * 375)
                sheet.getCell(row + 1, 6).setValue(Number(accIncome2021[row][0]) * 1000000 * 375)
                break;
            case "eHUF":
                sheet.getCell(row + 1, 4).setValue(Number(accIncome2020[row][0]) * 1000)
                sheet.getCell(row + 1, 6).setValue(Number(accIncome2021[row][0]) * 1000)
                break;
            case "mHUF":
                sheet.getCell(row + 1, 4).setValue(Number(accIncome2020[row][0]) * 1000000)
                sheet.getCell(row + 1, 6).setValue(Number(accIncome2021[row][0]) * 1000000)
                break;
            case "eEUR":
                sheet.getCell(row + 1, 4).setValue(Number(accIncome2020[row][0]) * 1000 * 375)
                sheet.getCell(row + 1, 6).setValue(Number(accIncome2021[row][0]) * 1000 * 375)
                break;
            case "EUR":
                sheet.getCell(row+1, 4).setValue(Number(accIncome2020[row][0]) * 375)
                sheet.getCell(row+1, 6).setValue(Number(accIncome2021[row][0]) * 375)
                break;
            case "100mHUF":
                sheet.getCell(row+1, 4).setValue(Number(accIncome2020[row][0]) * 100000000)
                sheet.getCell(row+1, 6).setValue(Number(accIncome2021[row][0]) * 100000000)
                break;
        } 
    }
}