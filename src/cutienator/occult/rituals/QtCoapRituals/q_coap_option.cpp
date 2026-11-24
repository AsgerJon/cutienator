//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/qcoapoption.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapoption_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapoption.cpp, line 344, as _ZN11QCoapOption6d_funcEv
inline QCoapOptionPrivate *QCoapOption::d_func()
{
    return d_ptr;
}
//  -----------------------------------------------------------------------

//  QCoapOption::QCoapOption(OptionName name, const QByteArray &opaqueValue)
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_ZN11QCoapOptionC1ENS_10OptionNameERK10QByteArray(
    QCoapOption::OptionName name,
    const QByteArray *opaqueValue) {
  return new QCoapOption(name, *opaqueValue);
}

//  QCoapOption::QCoapOption(OptionName name, const QString &stringValue)
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_ZN11QCoapOptionC1ENS_10OptionNameERK7QString(
    QCoapOption::OptionName name,
    const QString *stringValue) {
  return new QCoapOption(name, *stringValue);
}

//  QCoapOption::QCoapOption(OptionName name, quint32 intValue)
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_ZN11QCoapOptionC1ENS_10OptionNameEj(
    QCoapOption::OptionName name,
    quint32 intValue) {
  return new QCoapOption(name, intValue);
}

//  QCoapOption::QCoapOption(const QCoapOption &other)
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_ZN11QCoapOptionC1ERKS_(const QCoapOption *other) {
  return new QCoapOption(*other);
}

//  QCoapOption::~QCoapOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapOptionD1Ev(QCoapOption *self) {
  delete self;
}

//  QByteArray QCoapOption::opaqueValue() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QCoapOption11opaqueValueEv(const QCoapOption *self) {
  return new QByteArray(self->opaqueValue());
}

//  quint32 QCoapOption::uintValue() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK11QCoapOption9uintValueEv(const QCoapOption *self) {
  return self->uintValue();
}

//  QString QCoapOption::stringValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QCoapOption11stringValueEv(const QCoapOption *self) {
  return new QString(self->stringValue());
}

//  int QCoapOption::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QCoapOption6lengthEv(const QCoapOption *self) {
  return self->length();
}

//  OptionName QCoapOption::name() const
extern "C" Q_DECL_EXPORT
QCoapOption::OptionName ritual_ZNK11QCoapOption4nameEv(
    const QCoapOption *self) {
  return self->name();
}

//  bool QCoapOption::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QCoapOption7isValidEv(const QCoapOption *self) {
  return self->isValid();
}

//  bool QCoapOption::operator==(const QCoapOption &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QCoapOptioneqERKS_(
    const QCoapOption *self,
    const QCoapOption *other) {
  return self->operator==(*other);
}

//  bool QCoapOption::operator!=(const QCoapOption &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QCoapOptionneERKS_(
    const QCoapOption *self,
    const QCoapOption *other) {
  return self->operator!=(*other);
}

//  QCoapOptionPrivate *QCoapOption::d_func()
extern "C" Q_DECL_EXPORT
QCoapOptionPrivate *ritual_ZN11QCoapOption6d_funcEv(QCoapOption *self) {
  return self->d_func();
}

//  const QCoapOptionPrivate *QCoapOption::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapOptionPrivate *ritual_ZNK11QCoapOption6d_funcEv(
    const QCoapOption *self) {
  return self->d_func();
}

//  QList<QCoapOption>::QList()
extern "C" Q_DECL_EXPORT
QList<QCoapOption> *ritual_list_make_QCoapOption() {
  return new QList<QCoapOption>();
}

//  void QList<QCoapOption>::append(const QCoapOption &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCoapOption(
    QList<QCoapOption> *self,
    const QCoapOption *element) {
  self->append(*element);
}

//  qsizetype QList<QCoapOption>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCoapOption(const QList<QCoapOption> *self) {
  return self->size();
}

//  const QCoapOption &QList<QCoapOption>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_list_at_QCoapOption(
    const QList<QCoapOption> *self,
    long long index) {
  return new QCoapOption(self->at(index));
}

//  QList<QCoapOption>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCoapOption(QList<QCoapOption> *self) {
  delete self;
}
