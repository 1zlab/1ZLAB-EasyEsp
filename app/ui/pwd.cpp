#include "pwd.h"
#include "ui_pwd.h"

Pwd::Pwd(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Pwd)
{
    ui->setupUi(this);
}

Pwd::~Pwd()
{
    delete ui;
}
