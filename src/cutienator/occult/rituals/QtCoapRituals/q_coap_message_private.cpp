//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapmessage_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoapmessage_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapmessage.cpp, line 22, as _ZN19QCoapMessagePrivateD2Ev
inline QCoapMessagePrivate::~QCoapMessagePrivate()
{
}

//  from ../qtcoap/src/coap/qcoapmessage.cpp, line 26, as _ZNK19QCoapMessagePrivate5cloneEv
inline QCoapMessagePrivate *QCoapMessagePrivate::clone() const
{
    return new QCoapMessagePrivate(*this);
}
//  -----------------------------------------------------------------------

//  A QCoapMessagePrivate that Python can take functions over in. Every QCoapMessagePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCoapMessagePrivateCall0)(const void *, int *);
class CuteQCoapMessagePrivate : public QCoapMessagePrivate {
public:
  using QCoapMessagePrivate::QCoapMessagePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK19QCoapMessagePrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QCoapMessagePrivate *QCoapMessagePrivate::clone() const
  QCoapMessagePrivate *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapMessagePrivateCall0 call = reinterpret_cast<CuteQCoapMessagePrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCoapMessagePrivate *>(given);
    }
    return QCoapMessagePrivate::clone();
  }
};

//  QCoapMessagePrivate::~QCoapMessagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapMessagePrivateD1Ev(QCoapMessagePrivate *self) {
  delete self;
}

//  QCoapMessagePrivate *QCoapMessagePrivate::clone() const
extern "C" Q_DECL_EXPORT
QCoapMessagePrivate *ritual_ZNK19QCoapMessagePrivate5cloneEv(
    const QCoapMessagePrivate *self) {
  return self->clone();
}

//  a Python function taken by a CuteQCoapMessagePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapMessagePrivate(
    QCoapMessagePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapMessagePrivate *>(self)->take(key, call);
}
