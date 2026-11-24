//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/6.12.0/QtHelp/private/qhelpcollectionhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHelp/QtHelp>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHelp/6.12.0/QtHelp/private/qhelpcollectionhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhelpcollectionhandler_p.h"
#include "qhelp_global.h"
#include "qhelpdbreader_p.h"
#include "qhelpfilterdata.h"
#include "qhelplink.h"
#include <QtCore/qdatastream.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdir.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qset.h>
#include <QtCore/qtimer.h>
#include <QtCore/qversionnumber.h>
#include <QtSql/qsqldriver.h>
#include <QtSql/qsqlerror.h>
#include <QtSql/qsqlquery.h>
#include <algorithm>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 71, as _ZN22QHelpCollectionHandlerD1Ev
inline QHelpCollectionHandler::~QHelpCollectionHandler()
{
    closeDB();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 85, as _ZN22QHelpCollectionHandler7closeDBEv
inline void QHelpCollectionHandler::closeDB()
{
    if (!m_query)
        return;

    m_query.reset();
    QSqlDatabase::removeDatabase(m_connectionName);
    m_connectionName.clear();
}

//  from ../qttools/src/assistant/help/qhelpcollectionhandler.cpp, line 227, as _ZNK22QHelpCollectionHandler15absoluteDocPathERK7QString
inline QString QHelpCollectionHandler::absoluteDocPath(const QString &fileName) const
{
    const QFileInfo fi(collectionFile());
    return QDir::isAbsolutePath(fileName)
            ? fileName
            : QFileInfo(fi.absolutePath() + u'/' + fileName).absoluteFilePath();
}
//  -----------------------------------------------------------------------

//  A QHelpCollectionHandler that Python can take functions over in. Every QHelpCollectionHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpCollectionHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpCollectionHandlerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpCollectionHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpCollectionHandler : public QHelpCollectionHandler {
public:
  using QHelpCollectionHandler::QHelpCollectionHandler;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall0 call = reinterpret_cast<CuteQHelpCollectionHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall1 call = reinterpret_cast<CuteQHelpCollectionHandlerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall2 call = reinterpret_cast<CuteQHelpCollectionHandlerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall3 call = reinterpret_cast<CuteQHelpCollectionHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall4 call = reinterpret_cast<CuteQHelpCollectionHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall5 call = reinterpret_cast<CuteQHelpCollectionHandlerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHelpCollectionHandlerCall6 call = reinterpret_cast<CuteQHelpCollectionHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpCollectionHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QHelpCollectionHandler10metaObjectEv(
    const QHelpCollectionHandler *self) {
  return self->metaObject();
}

//  QHelpCollectionHandler::~QHelpCollectionHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandlerD1Ev(QHelpCollectionHandler *self) {
  delete self;
}

//  QString QHelpCollectionHandler::collectionFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHelpCollectionHandler14collectionFileEv(
    const QHelpCollectionHandler *self) {
  return new QString(self->collectionFile());
}

//  void QHelpCollectionHandler::setReadOnly(bool readOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler11setReadOnlyEb(
    QHelpCollectionHandler *self,
    bool readOnly) {
  self->setReadOnly(readOnly);
}

//  void QHelpCollectionHandler::closeDB()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHelpCollectionHandler7closeDBEv(
    QHelpCollectionHandler *self) {
  self->closeDB();
}

//  QString QHelpCollectionHandler::absoluteDocPath(const QString &fileName)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHelpCollectionHandler15absoluteDocPathERK7QString(
    const QHelpCollectionHandler *self,
    const QString *fileName) {
  return new QString(self->absoluteDocPath(*fileName));
}

//  a Python function taken by a CuteQHelpCollectionHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpCollectionHandler(
    QHelpCollectionHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpCollectionHandler *>(self)->take(key, call);
}
