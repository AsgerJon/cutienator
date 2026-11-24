//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlenumvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlenumvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QQmlEnumValue::QQmlEnumValue()
extern "C" Q_DECL_EXPORT
QQmlEnumValue *ritual_ZN13QQmlEnumValueC1Ev() {
  return new QQmlEnumValue();
}

//  QQmlEnumValue::QQmlEnumValue(const QString &n, int v)
extern "C" Q_DECL_EXPORT
QQmlEnumValue *ritual_ZN13QQmlEnumValueC1ERK7QStringi(
    const QString *n,
    int v) {
  return new QQmlEnumValue(*n, v);
}

//  QQmlEnumValue::~QQmlEnumValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlEnumValueD1Ev(QQmlEnumValue *self) {
  delete self;
}

//  QList<QQmlEnumValue>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlEnumValue> *ritual_list_make_QQmlEnumValue() {
  return new QList<QQmlEnumValue>();
}

//  void QList<QQmlEnumValue>::append(const QQmlEnumValue &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlEnumValue(
    QList<QQmlEnumValue> *self,
    const QQmlEnumValue *element) {
  self->append(*element);
}

//  qsizetype QList<QQmlEnumValue>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlEnumValue(const QList<QQmlEnumValue> *self) {
  return self->size();
}

//  const QQmlEnumValue &QList<QQmlEnumValue>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlEnumValue *ritual_list_at_QQmlEnumValue(
    const QList<QQmlEnumValue> *self,
    long long index) {
  return new QQmlEnumValue(self->at(index));
}

//  QList<QQmlEnumValue>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlEnumValue(QList<QQmlEnumValue> *self) {
  delete self;
}
