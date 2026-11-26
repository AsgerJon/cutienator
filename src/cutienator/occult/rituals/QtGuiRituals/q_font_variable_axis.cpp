//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfontvariableaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfontvariableaxis.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qfontvariableaxis.cpp, line 10, as local:qfontvariableaxis.cpp:QFontVariableAxisPrivate
class QFontVariableAxisPrivate : public QSharedData
{
public:
    QFont::Tag tag;
    QString name;
    qreal minimumValue = 0.0;
    qreal maximumValue = 0.0;
    qreal defaultValue = 0.0;
};

//  from src/gui/text/qfontvariableaxis.cpp, line 266, as _ZN17QFontVariableAxis6detachEv
inline void QFontVariableAxis::detach()
{
    d_ptr.detach();
}
//  -----------------------------------------------------------------------

//  QFontVariableAxisPrivate *QFontVariableAxis::d_func()
extern "C" Q_DECL_EXPORT
QFontVariableAxisPrivate *ritual_ZN17QFontVariableAxis6d_funcEv(
    QFontVariableAxis *self) {
  return self->d_func();
}

//  const QFontVariableAxisPrivate *QFontVariableAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QFontVariableAxisPrivate *ritual_ZNK17QFontVariableAxis6d_funcEv(
    const QFontVariableAxis *self) {
  return self->d_func();
}

//  QFontVariableAxis::QFontVariableAxis()
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_ZN17QFontVariableAxisC1Ev() {
  return new QFontVariableAxis();
}

//  QFontVariableAxis::QFontVariableAxis(QFontVariableAxis &&other)
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_ZN17QFontVariableAxisC1EOS_(
    QFontVariableAxis *other) {
  return new QFontVariableAxis(std::move(*other));
}

//  QFontVariableAxis::QFontVariableAxis(const QFontVariableAxis &axis)
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_ZN17QFontVariableAxisC1ERKS_(
    const QFontVariableAxis *axis) {
  return new QFontVariableAxis(*axis);
}

//  QFontVariableAxis::~QFontVariableAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxisD1Ev(QFontVariableAxis *self) {
  delete self;
}

//  QFontVariableAxis &QFontVariableAxis::operator=(QFontVariableAxis
//      &&other)
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_ZN17QFontVariableAxisaSEOS_(
    QFontVariableAxis *self,
    QFontVariableAxis *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QFontVariableAxis::swap(QFontVariableAxis &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis4swapERS_(
    QFontVariableAxis *self,
    QFontVariableAxis *other) {
  self->swap(*other);
}

//  QFontVariableAxis &QFontVariableAxis::operator=(const QFontVariableAxis
//      &axis)
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_ZN17QFontVariableAxisaSERKS_(
    QFontVariableAxis *self,
    const QFontVariableAxis *axis) {
  return &(self->operator=(*axis));
}

//  QFont::Tag QFontVariableAxis::tag() const
extern "C" Q_DECL_EXPORT
QFont::Tag *ritual_ZNK17QFontVariableAxis3tagEv(
    const QFontVariableAxis *self) {
  return new QFont::Tag(self->tag());
}

//  void QFontVariableAxis::setTag(QFont::Tag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis6setTagEN5QFont3TagE(
    QFontVariableAxis *self,
    const QFont::Tag *tag) {
  self->setTag(*tag);
}

//  QString QFontVariableAxis::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QFontVariableAxis4nameEv(
    const QFontVariableAxis *self) {
  return new QString(self->name());
}

//  void QFontVariableAxis::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis7setNameERK7QString(
    QFontVariableAxis *self,
    const QString *name) {
  self->setName(*name);
}

//  qreal QFontVariableAxis::minimumValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QFontVariableAxis12minimumValueEv(
    const QFontVariableAxis *self) {
  return self->minimumValue();
}

//  void QFontVariableAxis::setMinimumValue(qreal minimumValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis15setMinimumValueEd(
    QFontVariableAxis *self,
    qreal minimumValue) {
  self->setMinimumValue(minimumValue);
}

//  qreal QFontVariableAxis::maximumValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QFontVariableAxis12maximumValueEv(
    const QFontVariableAxis *self) {
  return self->maximumValue();
}

//  void QFontVariableAxis::setMaximumValue(qreal maximumValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis15setMaximumValueEd(
    QFontVariableAxis *self,
    qreal maximumValue) {
  self->setMaximumValue(maximumValue);
}

//  qreal QFontVariableAxis::defaultValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QFontVariableAxis12defaultValueEv(
    const QFontVariableAxis *self) {
  return self->defaultValue();
}

//  void QFontVariableAxis::setDefaultValue(qreal defaultValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis15setDefaultValueEd(
    QFontVariableAxis *self,
    qreal defaultValue) {
  self->setDefaultValue(defaultValue);
}

//  QByteArray QFontVariableAxis::tagString() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QFontVariableAxis9tagStringEv(
    const QFontVariableAxis *self) {
  return new QByteArray(self->tagString());
}

//  void QFontVariableAxis::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis6detachEv(QFontVariableAxis *self) {
  self->detach();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QFontVariableAxis &axis)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK17QFontVariableAxis(
    const QDebug *debug,
    const QFontVariableAxis *axis) {
  return new QDebug(operator<<(*debug, *axis));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QFontVariableAxis>::QList()
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_list_make_QFontVariableAxis() {
  return new QList<QFontVariableAxis>();
}

//  void QList<QFontVariableAxis>::append(const QFontVariableAxis &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QFontVariableAxis(
    QList<QFontVariableAxis> *self,
    const QFontVariableAxis *element) {
  self->append(*element);
}

//  qsizetype QList<QFontVariableAxis>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QFontVariableAxis(
    const QList<QFontVariableAxis> *self) {
  return self->size();
}

//  const QFontVariableAxis &QList<QFontVariableAxis>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_list_at_QFontVariableAxis(
    const QList<QFontVariableAxis> *self,
    long long index) {
  return new QFontVariableAxis(self->at(index));
}

//  QList<QFontVariableAxis>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QFontVariableAxis(QList<QFontVariableAxis> *self) {
  delete self;
}
