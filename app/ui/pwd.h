#ifndef PWD_H
#define PWD_H

#include <QWidget>

namespace Ui {
class Pwd;
}

class Pwd : public QWidget
{
    Q_OBJECT

public:
    explicit Pwd(QWidget *parent = nullptr);
    ~Pwd();

private:
    Ui::Pwd *ui;
};

#endif // PWD_H
