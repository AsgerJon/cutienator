//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdatetimeedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdatetimeedit.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>

//  const QMetaObject *QDateEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QDateEdit10metaObjectEv(
    const QDateEdit *self) {
  return self->metaObject();
}

//  QString QDateEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QDateEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDateEdit::tr(s, c, n));
}

//  QDateEdit::QDateEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateEdit *ritual_ZN9QDateEditC1EP7QWidget(QWidget *parent) {
  return new QDateEdit(parent);
}

//  QDateEdit::QDateEdit(QDate date, QWidget *parent)
extern "C" Q_DECL_EXPORT
QDateEdit *ritual_ZN9QDateEditC1E5QDateP7QWidget(
    const QDate *date,
    QWidget *parent) {
  return new QDateEdit(*date, parent);
}

//  QDateEdit::~QDateEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QDateEditD1Ev(QDateEdit *self) {
  delete self;
}
