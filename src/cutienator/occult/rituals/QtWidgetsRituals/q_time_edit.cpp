//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdatetimeedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdatetimeedit.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>

//  const QMetaObject *QTimeEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTimeEdit10metaObjectEv(
    const QTimeEdit *self) {
  return self->metaObject();
}

//  QString QTimeEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTimeEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTimeEdit::tr(s, c, n));
}

//  QTimeEdit::QTimeEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTimeEdit *ritual_ZN9QTimeEditC1EP7QWidget(QWidget *parent) {
  return new QTimeEdit(parent);
}

//  QTimeEdit::QTimeEdit(QTime time, QWidget *parent)
extern "C" Q_DECL_EXPORT
QTimeEdit *ritual_ZN9QTimeEditC1E5QTimeP7QWidget(
    const QTime *time,
    QWidget *parent) {
  return new QTimeEdit(*time, parent);
}

//  QTimeEdit::~QTimeEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTimeEditD1Ev(QTimeEdit *self) {
  delete self;
}
