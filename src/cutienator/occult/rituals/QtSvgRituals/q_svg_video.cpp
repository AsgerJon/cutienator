//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/private/qsvggraphics_p.h>
#include <QtSvg/private/qsvgstructure_p.h>
#include <QtSvg/private/qsvgfont_p.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qpainter.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qfixed_p.h>
#include <QtCore/QElapsedTimer>
#include <QtCore/QLoggingCategory>
#include <math.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtsvg/src/svg/qsvggraphics.cpp, line 694, as _ZNK9QSvgVideo4typeEv
inline QSvgNode::Type QSvgVideo::type() const
{
    return Video;
}
//  -----------------------------------------------------------------------

//  A QSvgVideo that Python can take functions over in. Every QSvgVideo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgVideoCall0)(const void *, int *);
typedef bool (*CuteQSvgVideoCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgVideoCall2)(const void *, int *);
class CuteQSvgVideo : public QSvgVideo {
public:
  using QSvgVideo::QSvgVideo;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgVideo::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgVideoCall0 call = reinterpret_cast<CuteQSvgVideoCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgVideo::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgVideoCall1 call = reinterpret_cast<CuteQSvgVideoCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgVideoCall2 call = reinterpret_cast<CuteQSvgVideoCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgVideo::~QSvgVideo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgVideoD1Ev(QSvgVideo *self) {
  delete self;
}

//  void QSvgVideo::drawCommand(QPainter *a0, QSvgExtraStates &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgVideo11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgVideo *self,
    QPainter *a0,
    QSvgExtraStates *a1) {
  self->drawCommand(a0, *a1);
}

//  Type QSvgVideo::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK9QSvgVideo4typeEv(const QSvgVideo *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgVideo, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgVideo(QSvgVideo *self, const char *key, void *call) {
  return static_cast<CuteQSvgVideo *>(self)->take(key, call);
}

//  Type QSvgVideo::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK9QSvgVideo4typeEv(const QSvgVideo *self) {
  return self->QSvgVideo::type();
}
