#ifndef ANALYSIS3_H
#define ANALYSIS3_H

#include <QDialog>

namespace Ui {
class analysis3;
}

class analysis3 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis3(QWidget *parent = 0);
    ~analysis3();

private:
    Ui::analysis3 *ui;
};

#endif // ANALYSIS3_H
