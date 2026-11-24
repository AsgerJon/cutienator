//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideonode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideonode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/private/qsgvideonode_p.h>
#include <QtMultimedia/private/qhwvideobuffer_p.h>
#include <QtMultimedia/private/qvideoframetexturepool_p.h>
#include <QtMultimedia/private/qvideotexturehelper_p.h>
#include <QtMultimediaQuick/private/qsgvideotexture_p.h>
#include <QtMultimediaQuick/private/qquickvideooutput_p.h>
#include <QtQuick/qsgmaterial.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsginternaltextnode_p.h>
#if QT_CONFIG(opengles2)
#include <QtGui/private/qshaderdescription_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimediaquick/qsgvideonode_p.cpp, line 266, as _ZN12QSGVideoNodeD1Ev
inline QSGVideoNode::~QSGVideoNode()
{
    delete m_subtitleTextNode;
}
//  -----------------------------------------------------------------------

//  A QSGVideoNode that Python can take functions over in. Every QSGVideoNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGVideoNodeCall0)(const void *, int *);
typedef void (*CuteQSGVideoNodeCall1)(const void *, int *);
class CuteQSGVideoNode : public QSGVideoNode {
public:
  using QSGVideoNode::QSGVideoNode;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGVideoNodeCall0 call = reinterpret_cast<CuteQSGVideoNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGVideoNodeCall1 call = reinterpret_cast<CuteQSGVideoNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGVideoNode::~QSGVideoNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGVideoNodeD1Ev(QSGVideoNode *self) {
  delete self;
}

//  QVideoFrameFormat::PixelFormat QSGVideoNode::pixelFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::PixelFormat ritual_ZNK12QSGVideoNode11pixelFormatEv(
    const QSGVideoNode *self) {
  return self->pixelFormat();
}

//  a Python function taken by a CuteQSGVideoNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGVideoNode(
    QSGVideoNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGVideoNode *>(self)->take(key, call);
}
