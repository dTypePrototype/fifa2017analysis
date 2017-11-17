#ifndef ANALYSIS6_H
#define ANALYSIS6_H

#include <QDialog>

namespace Ui {
class analysis6;
}

class analysis6 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis6(QWidget *parent = 0);
    ~analysis6();

private:
    Ui::analysis6 *ui;
};

#endif // ANALYSIS6_H
