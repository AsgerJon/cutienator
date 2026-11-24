//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  bool operator==(const QQmlJSDocumentEdit &lhs, const QQmlJSDocumentEdit
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QQmlJSDocumentEditS1_(
    const QQmlJSDocumentEdit *lhs,
    const QQmlJSDocumentEdit *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QQmlJSDocumentEdit &lhs, const QQmlJSDocumentEdit
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QQmlJSDocumentEditS1_(
    const QQmlJSDocumentEdit *lhs,
    const QQmlJSDocumentEdit *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QQmlJSDocumentEdit::~QQmlJSDocumentEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSDocumentEditD1Ev(QQmlJSDocumentEdit *self) {
  delete self;
}

//  QList<QQmlJSDocumentEdit>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlJSDocumentEdit> *ritual_list_make_QQmlJSDocumentEdit() {
  return new QList<QQmlJSDocumentEdit>();
}

//  void QList<QQmlJSDocumentEdit>::append(const QQmlJSDocumentEdit &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlJSDocumentEdit(
    QList<QQmlJSDocumentEdit> *self,
    const QQmlJSDocumentEdit *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlJSDocumentEdit>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlJSDocumentEdit(
    const QList<QQmlJSDocumentEdit> *self) {
  return self->size();
}

//  const QQmlJSDocumentEdit &QList<QQmlJSDocumentEdit>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQmlJSDocumentEdit *ritual_list_at_QQmlJSDocumentEdit(
    const QList<QQmlJSDocumentEdit> *self,
    long long index) {
  return new QQmlJSDocumentEdit(self->at(index));
}

//  QList<QQmlJSDocumentEdit>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlJSDocumentEdit(QList<QQmlJSDocumentEdit> *self) {
  delete self;
}
