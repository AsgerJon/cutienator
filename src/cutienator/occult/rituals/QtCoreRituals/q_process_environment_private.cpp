//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(processenvironment)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qprocess_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qprocess.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qdebug.h>
#include <qdir.h>
#include <qscopedvaluerollback.h>
#include "qprocess.h"
#include "qprocess_p.h"
#include <qbytearray.h>
#include <qdeadlinetimer.h>
#include <qcoreapplication.h>
#if __has_include(<paths.h>)
#include <paths.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qprocess.cpp, line 78, as _ZN26QProcessEnvironmentPrivate8fromListERK5QListI7QStringE
inline QProcessEnvironment QProcessEnvironmentPrivate::fromList(const QStringList &list)
{
    QProcessEnvironment env;
    QStringList::ConstIterator it = list.constBegin(),
                              end = list.constEnd();
    for ( ; it != end; ++it) {
        const qsizetype pos = it->indexOf(u'=', 1);
        if (pos < 1)
            continue;

        QString value = it->mid(pos + 1);
        QString name = *it;
        name.truncate(pos);
        env.insert(name, value);
    }
    return env;
}

//  from src/corelib/io/qprocess.cpp, line 69, as _ZNK26QProcessEnvironmentPrivate6toListEv
inline QStringList QProcessEnvironmentPrivate::toList() const
{
    QStringList result;
    result.reserve(vars.size());
    for (auto it = vars.cbegin(), end = vars.cend(); it != end; ++it)
        result << nameToString(it.key()) + u'=' + valueToString(it.value());
    return result;
}

//  from src/corelib/io/qprocess.cpp, line 96, as _ZNK26QProcessEnvironmentPrivate4keysEv
inline QStringList QProcessEnvironmentPrivate::keys() const
{
    QStringList result;
    result.reserve(vars.size());
    auto it = vars.constBegin();
    const auto end = vars.constEnd();
    for ( ; it != end; ++it)
        result << nameToString(it.key());
    return result;
}

//  from src/corelib/io/qprocess.cpp, line 107, as _ZN26QProcessEnvironmentPrivate6insertERKS_
inline void QProcessEnvironmentPrivate::insert(const QProcessEnvironmentPrivate &other)
{
    auto it = other.vars.constBegin();
    const auto end = other.vars.constEnd();
    for ( ; it != end; ++it)
        vars.insert(it.key(), it.value());

#ifdef Q_OS_UNIX
    auto nit = other.nameMap.constBegin();
    const auto nend = other.nameMap.constEnd();
    for ( ; nit != nend; ++nit)
        nameMap.insert(nit.key(), nit.value());
#endif
}
//  -----------------------------------------------------------------------

#if !(defined(Q_OS_WIN))
//  Key QProcessEnvironmentPrivate::prepareName(const QString &name) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK26QProcessEnvironmentPrivate11prepareNameERK7QString(
    const QProcessEnvironmentPrivate *self,
    const QString *name) {
  return new QByteArray(self->prepareName(*name));
}
#endif  // !(defined(Q_OS_WIN))

#if !(defined(Q_OS_WIN))
//  QString QProcessEnvironmentPrivate::nameToString(const Key &name) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QProcessEnvironmentPrivate12nameToStringERK10QByteArray(
    const QProcessEnvironmentPrivate *self,
    const QByteArray *name) {
  return new QString(self->nameToString(*name));
}
#endif  // !(defined(Q_OS_WIN))

#if !(defined(Q_OS_WIN))
//  Value QProcessEnvironmentPrivate::prepareValue(const QString &value)
//      const
extern "C" Q_DECL_EXPORT
QProcEnvValue *ritual_ZNK26QProcessEnvironmentPrivate12prepareValueERK7QString(
    const QProcessEnvironmentPrivate *self,
    const QString *value) {
  return new QProcEnvValue(self->prepareValue(*value));
}
#endif  // !(defined(Q_OS_WIN))

#if !(defined(Q_OS_WIN))
//  QString QProcessEnvironmentPrivate::valueToString(const Value &value)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QProcessEnvironmentPrivate13valueToStringERK13QProcEnvValue(
    const QProcessEnvironmentPrivate *self,
    const QProcEnvValue *value) {
  return new QString(self->valueToString(*value));
}
#endif  // !(defined(Q_OS_WIN))

#if !(defined(Q_OS_WIN))
//  QProcessEnvironmentPrivate::QProcessEnvironmentPrivate()
extern "C" Q_DECL_EXPORT
QProcessEnvironmentPrivate *ritual_ZN26QProcessEnvironmentPrivateC1Ev() {
  return new QProcessEnvironmentPrivate();
}
#endif  // !(defined(Q_OS_WIN))

#if !(defined(Q_OS_WIN))
//  QProcessEnvironmentPrivate::QProcessEnvironmentPrivate(const
//      QProcessEnvironmentPrivate &other)
extern "C" Q_DECL_EXPORT
QProcessEnvironmentPrivate *ritual_ZN26QProcessEnvironmentPrivateC1ERKS_(
    const QProcessEnvironmentPrivate *other) {
  return new QProcessEnvironmentPrivate(*other);
}
#endif  // !(defined(Q_OS_WIN))

//  QProcessEnvironment QProcessEnvironmentPrivate::fromList(const
//      QStringList &list)
extern "C" Q_DECL_EXPORT
QProcessEnvironment *ritual_ZN26QProcessEnvironmentPrivate8fromListERK5QListI7QStringE(
    const QList<QString> *list) {
  return new QProcessEnvironment(
      QProcessEnvironmentPrivate::fromList(
          *list));
}

//  QStringList QProcessEnvironmentPrivate::toList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QProcessEnvironmentPrivate6toListEv(
    const QProcessEnvironmentPrivate *self) {
  return new QList<QString>(self->toList());
}

//  QStringList QProcessEnvironmentPrivate::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QProcessEnvironmentPrivate4keysEv(
    const QProcessEnvironmentPrivate *self) {
  return new QList<QString>(self->keys());
}

//  void QProcessEnvironmentPrivate::insert(const QProcessEnvironmentPrivate
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QProcessEnvironmentPrivate6insertERKS_(
    QProcessEnvironmentPrivate *self,
    const QProcessEnvironmentPrivate *other) {
  self->insert(*other);
}

//  QProcessEnvironmentPrivate::~QProcessEnvironmentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QProcessEnvironmentPrivateD1Ev(
    QProcessEnvironmentPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(processenvironment)
