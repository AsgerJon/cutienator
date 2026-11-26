//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qtextobject.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qchar.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextobject.h>
#include <QtGui/private/qtextobject_p.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextformat_p.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextlist.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextobject.cpp, line 491, as _ZN17QTextFramePrivate13fragmentAddedE5QCharj
inline void QTextFramePrivate::fragmentAdded(QChar type, uint fragment)
{
    if (type == QTextBeginningOfFrame) {
        Q_ASSERT(!fragment_start);
        fragment_start = fragment;
    } else if (type == QTextEndOfFrame) {
        Q_ASSERT(!fragment_end);
        fragment_end = fragment;
    } else if (type == QChar::ObjectReplacementCharacter) {
        Q_ASSERT(!fragment_start);
        Q_ASSERT(!fragment_end);
        fragment_start = fragment;
        fragment_end = fragment;
    } else {
        Q_ASSERT(false);
    }
}

//  from src/gui/text/qtextobject.cpp, line 509, as _ZN17QTextFramePrivate15fragmentRemovedE5QCharj
inline void QTextFramePrivate::fragmentRemoved(QChar type, uint fragment)
{
    Q_UNUSED(fragment); // --release warning
    if (type == QTextBeginningOfFrame) {
        Q_ASSERT(fragment_start == fragment);
        fragment_start = 0;
    } else if (type == QTextEndOfFrame) {
        Q_ASSERT(fragment_end == fragment);
        fragment_end = 0;
    } else if (type == QChar::ObjectReplacementCharacter) {
        Q_ASSERT(fragment_start == fragment);
        Q_ASSERT(fragment_end == fragment);
        fragment_start = 0;
        fragment_end = 0;
    } else {
        Q_ASSERT(false);
    }
    remove_me();
}

//  from src/gui/text/qtextobject.cpp, line 530, as _ZN17QTextFramePrivate9remove_meEv
inline void QTextFramePrivate::remove_me()
{
    Q_Q(QTextFrame);
    if (fragment_start == 0 && fragment_end == 0
        && !parentFrame) {
        QTextDocumentPrivate::get(q->document())->deleteObject(q);
        return;
    }

    if (!parentFrame)
        return;

    int index = parentFrame->d_func()->childFrames.indexOf(q);

    // iterator over all children and move them to the parent
    for (int i = 0; i < childFrames.size(); ++i) {
        QTextFrame *c = childFrames.at(i);
        parentFrame->d_func()->childFrames.insert(index, c);
        c->d_func()->parentFrame = parentFrame;
        ++index;
    }
    Q_ASSERT(parentFrame->d_func()->childFrames.at(index) == q);
    parentFrame->d_func()->childFrames.removeAt(index);

    childFrames.clear();
    parentFrame = nullptr;
}
//  -----------------------------------------------------------------------

//  A QTextFramePrivate that Python can take functions over in. Every QTextFramePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTextFramePrivateCall0)(const void *, const QChar *, uint, int *);
typedef void (*CuteQTextFramePrivateCall1)(const void *, const QChar *, uint, int *);
class CuteQTextFramePrivate : public QTextFramePrivate {
public:
  using QTextFramePrivate::QTextFramePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QTextFramePrivate13fragmentAddedE5QCharj")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QTextFramePrivate15fragmentRemovedE5QCharj")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QTextFramePrivate::fragmentAdded(QChar type, uint fragment)
  void fragmentAdded(QChar type, uint fragment) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextFramePrivateCall0 call = reinterpret_cast<CuteQTextFramePrivateCall0>(taken[0]);
      call(this, &type, fragment, &handled);
      if (handled) return;
    }
    QTextFramePrivate::fragmentAdded(type, fragment);
  }

  //  void QTextFramePrivate::fragmentRemoved(QChar type, uint fragment)
  void fragmentRemoved(QChar type, uint fragment) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextFramePrivateCall1 call = reinterpret_cast<CuteQTextFramePrivateCall1>(taken[1]);
      call(this, &type, fragment, &handled);
      if (handled) return;
    }
    QTextFramePrivate::fragmentRemoved(type, fragment);
  }
};

//  QTextFrame *QTextFramePrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZN17QTextFramePrivate6q_funcEv(QTextFramePrivate *self) {
  return self->q_func();
}

//  const QTextFrame *QTextFramePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextFrame *ritual_ZNK17QTextFramePrivate6q_funcEv(
    const QTextFramePrivate *self) {
  return self->q_func();
}

//  QTextFramePrivate::QTextFramePrivate(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextFramePrivate *ritual_ZN17QTextFramePrivateC1EP13QTextDocument(
    QTextDocument *doc) {
  return new CuteQTextFramePrivate(doc);
}

//  void QTextFramePrivate::fragmentAdded(QChar type, uint fragment)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextFramePrivate13fragmentAddedE5QCharj(
    QTextFramePrivate *self,
    const QChar *type,
    uint fragment) {
  self->fragmentAdded(*type, fragment);
}

//  void QTextFramePrivate::fragmentRemoved(QChar type, uint fragment)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextFramePrivate15fragmentRemovedE5QCharj(
    QTextFramePrivate *self,
    const QChar *type,
    uint fragment) {
  self->fragmentRemoved(*type, fragment);
}

//  void QTextFramePrivate::remove_me()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextFramePrivate9remove_meEv(QTextFramePrivate *self) {
  self->remove_me();
}

//  a Python function taken by a CuteQTextFramePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextFramePrivate(
    QTextFramePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextFramePrivate *>(self)->take(key, call);
}

//  void QTextFramePrivate::fragmentAdded(QChar type, uint fragment)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTextFramePrivate13fragmentAddedE5QCharj(
    QTextFramePrivate *self,
    const QChar *type,
    uint fragment) {
  self->QTextFramePrivate::fragmentAdded(*type, fragment);
}

//  void QTextFramePrivate::fragmentRemoved(QChar type, uint fragment)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTextFramePrivate15fragmentRemovedE5QCharj(
    QTextFramePrivate *self,
    const QChar *type,
    uint fragment) {
  self->QTextFramePrivate::fragmentRemoved(*type, fragment);
}
