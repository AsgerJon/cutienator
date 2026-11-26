//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/qcoapmessage.h>
#include <QtCore/qbytearray.h>
#include <QtCoap/qcoapoption.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapmessage.cpp, line 410, as _ZN12QCoapMessage6d_funcEv
inline QCoapMessagePrivate* QCoapMessage::d_func()
{
    return d_ptr.data();
}
//  -----------------------------------------------------------------------

//  QCoapMessage::QCoapMessage()
extern "C" Q_DECL_EXPORT
QCoapMessage *ritual_ZN12QCoapMessageC1Ev() {
  return new QCoapMessage();
}

//  QCoapMessage::QCoapMessage(const QCoapMessage &other)
extern "C" Q_DECL_EXPORT
QCoapMessage *ritual_ZN12QCoapMessageC1ERKS_(const QCoapMessage *other) {
  return new QCoapMessage(*other);
}

//  QCoapMessage::~QCoapMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessageD1Ev(QCoapMessage *self) {
  delete self;
}

//  void QCoapMessage::swap(QCoapMessage &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage4swapERS_(
    QCoapMessage *self,
    QCoapMessage *other) {
  self->swap(*other);
}

//  QCoapMessage &QCoapMessage::operator=(const QCoapMessage &other)
extern "C" Q_DECL_EXPORT
QCoapMessage *ritual_ZN12QCoapMessageaSERKS_(
    QCoapMessage *self,
    const QCoapMessage *other) {
  return &(self->operator=(*other));
}

//  QCoapMessage &QCoapMessage::operator=(QCoapMessage &&other)
extern "C" Q_DECL_EXPORT
QCoapMessage *ritual_ZN12QCoapMessageaSEOS_(
    QCoapMessage *self,
    QCoapMessage *other) {
  return &(self->operator=(std::move(*other)));
}

//  quint8 QCoapMessage::version() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK12QCoapMessage7versionEv(const QCoapMessage *self) {
  return self->version();
}

//  Type QCoapMessage::type() const
extern "C" Q_DECL_EXPORT
QCoapMessage::Type ritual_ZNK12QCoapMessage4typeEv(
    const QCoapMessage *self) {
  return self->type();
}

//  QByteArray QCoapMessage::token() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QCoapMessage5tokenEv(const QCoapMessage *self) {
  return new QByteArray(self->token());
}

//  quint8 QCoapMessage::tokenLength() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK12QCoapMessage11tokenLengthEv(const QCoapMessage *self) {
  return self->tokenLength();
}

//  quint16 QCoapMessage::messageId() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK12QCoapMessage9messageIdEv(const QCoapMessage *self) {
  return self->messageId();
}

//  QByteArray QCoapMessage::payload() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QCoapMessage7payloadEv(const QCoapMessage *self) {
  return new QByteArray(self->payload());
}

//  void QCoapMessage::setVersion(quint8 version)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage10setVersionEh(
    QCoapMessage *self,
    quint8 version) {
  self->setVersion(version);
}

//  void QCoapMessage::setType(const Type &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage7setTypeERKNS_4TypeE(
    QCoapMessage *self,
    const QCoapMessage::Type *type) {
  self->setType(*type);
}

//  void QCoapMessage::setToken(const QByteArray &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage8setTokenERK10QByteArray(
    QCoapMessage *self,
    const QByteArray *token) {
  self->setToken(*token);
}

//  void QCoapMessage::setMessageId(quint16 a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage12setMessageIdEt(
    QCoapMessage *self,
    quint16 a0) {
  self->setMessageId(a0);
}

//  void QCoapMessage::setPayload(const QByteArray &payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage10setPayloadERK10QByteArray(
    QCoapMessage *self,
    const QByteArray *payload) {
  self->setPayload(*payload);
}

//  void QCoapMessage::setOptions(const QList<QCoapOption> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage10setOptionsERK5QListI11QCoapOptionE(
    QCoapMessage *self,
    const QList<QCoapOption> *options) {
  self->setOptions(*options);
}

//  QCoapOption QCoapMessage::optionAt(int index) const
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_ZNK12QCoapMessage8optionAtEi(
    const QCoapMessage *self,
    int index) {
  return new QCoapOption(self->optionAt(index));
}

//  QCoapOption QCoapMessage::option(QCoapOption::OptionName name) const
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_ZNK12QCoapMessage6optionEN11QCoapOption10OptionNameE(
    const QCoapMessage *self,
    QCoapOption::OptionName name) {
  return new QCoapOption(self->option(name));
}

//  bool QCoapMessage::hasOption(QCoapOption::OptionName name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QCoapMessage9hasOptionEN11QCoapOption10OptionNameE(
    const QCoapMessage *self,
    QCoapOption::OptionName name) {
  return self->hasOption(name);
}

//  const QList<QCoapOption> &QCoapMessage::options() const
extern "C" Q_DECL_EXPORT
QList<QCoapOption> *ritual_ZNK12QCoapMessage7optionsEv(
    const QCoapMessage *self) {
  return new QList<QCoapOption>(self->options());
}

//  QList<QCoapOption> QCoapMessage::options(QCoapOption::OptionName name)
//      const
extern "C" Q_DECL_EXPORT
QList<QCoapOption> *ritual_ZNK12QCoapMessage7optionsEN11QCoapOption10OptionNameE(
    const QCoapMessage *self,
    QCoapOption::OptionName name) {
  return new QList<QCoapOption>(self->options(name));
}

//  int QCoapMessage::optionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QCoapMessage11optionCountEv(const QCoapMessage *self) {
  return self->optionCount();
}

//  void QCoapMessage::addOption(QCoapOption::OptionName name, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage9addOptionEN11QCoapOption10OptionNameERK10QByteArray(
    QCoapMessage *self,
    QCoapOption::OptionName name,
    const QByteArray *value) {
  self->addOption(name, *value);
}

//  void QCoapMessage::addOption(const QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage9addOptionERK11QCoapOption(
    QCoapMessage *self,
    const QCoapOption *option) {
  self->addOption(*option);
}

//  void QCoapMessage::removeOption(const QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage12removeOptionERK11QCoapOption(
    QCoapMessage *self,
    const QCoapOption *option) {
  self->removeOption(*option);
}

//  void QCoapMessage::removeOption(QCoapOption::OptionName name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage12removeOptionEN11QCoapOption10OptionNameE(
    QCoapMessage *self,
    QCoapOption::OptionName name) {
  self->removeOption(name);
}

//  void QCoapMessage::clearOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QCoapMessage12clearOptionsEv(QCoapMessage *self) {
  self->clearOptions();
}

//  QCoapMessage::QCoapMessage(QCoapMessagePrivate &dd)
extern "C" Q_DECL_EXPORT
QCoapMessage *ritual_ZN12QCoapMessageC1ER19QCoapMessagePrivate(
    QCoapMessagePrivate *dd) {
  return new QCoapMessage(*dd);
}

//  QCoapMessagePrivate *QCoapMessage::d_func()
extern "C" Q_DECL_EXPORT
QCoapMessagePrivate *ritual_ZN12QCoapMessage6d_funcEv(QCoapMessage *self) {
  return self->d_func();
}

//  const QCoapMessagePrivate *QCoapMessage::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapMessagePrivate *ritual_ZNK12QCoapMessage6d_funcEv(
    const QCoapMessage *self) {
  return self->d_func();
}
