//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhostinfo.h"
#include "qhostinfo_p.h"
#include <qplatformdefs.h>
#include "QtCore/qapplicationstatic.h"
#include <qabstracteventdispatcher.h>
#include <qcoreapplication.h>
#include <qmetaobject.h>
#include <qscopeguard.h>
#include <qstringlist.h>
#include <qthread.h>
#include <qurl.h>
#include <private/qobject_p.h>
#include <algorithm>
#ifdef Q_OS_UNIX
#  include <unistd.h>
#  include <netdb.h>
#  include <netinet/in.h>
#elif defined Q_OS_WIN
#  include <ws2tcpip.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/kernel/qhostinfo.cpp, line 836, as _ZN17QHostInfoRunnableD1Ev
inline QHostInfoRunnable::~QHostInfoRunnable()
{
    // resultEmitter belongs to the receiver's thread, which is rarely the one deleting this
    // runnable, so it can't be destroyed here directly.
    QObjectPrivate::deleteInOwnThread(resultEmitter.release());
}
//  -----------------------------------------------------------------------

//  A QHostInfoRunnable that Python can take functions over in. Every QHostInfoRunnable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHostInfoRunnableCall0)(const void *, int *);
class CuteQHostInfoRunnable : public QHostInfoRunnable {
public:
  using QHostInfoRunnable::QHostInfoRunnable;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QRunnable3runEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QHostInfoRunnable::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQHostInfoRunnableCall0 call = reinterpret_cast<CuteQHostInfoRunnableCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QHostInfoRunnable::run();
  }
};

//  QHostInfoRunnable::~QHostInfoRunnable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHostInfoRunnableD1Ev(QHostInfoRunnable *self) {
  delete self;
}

//  a Python function taken by a CuteQHostInfoRunnable, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHostInfoRunnable(
    QHostInfoRunnable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHostInfoRunnable *>(self)->take(key, call);
}
