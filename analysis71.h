#ifndef ANALYSIS71_H
#define ANALYSIS71_H

#include <QDialog>

namespace Ui {
class analysis71;
}

class analysis71 : public QDialog
{
    Q_OBJECT

public:
    explicit analysis71(QWidget *parent = 0);
    ~analysis71();

private slots:
    void on_nextButton_clicked();

private:
    Ui::analysis71 *ui;
};

#endif // ANALYSIS71_H
