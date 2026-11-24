//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpicture_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpicture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qpicture.h"
#include <private/qpicture_p.h>
#ifndef QT_NO_PICTURE
#include <private/qfactoryloader_p.h>
#include <private/qpaintengine_pic_p.h>
#include <private/qfont_p.h>
#include <qguiapplication.h>
#include "qdatastream.h"
#include "qfile.h"
#include "qimage.h"
#include "qmutex.h"
#include "qpainter.h"
#include "qpainterpath.h"
#include "qpixmap.h"
#include "qregion.h"
#include "qdebug.h"
#include <QtCore/private/qlocking_p.h>
#include <algorithm>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qpicture.cpp, line 973, as _ZN15QPicturePrivateC1Ev
#if !defined(QT_NO_PICTURE)
inline QPicturePrivate::QPicturePrivate()
    : pictb(&pictbData),
      in_memory_only(false)
{
}
#endif  // !defined(QT_NO_PICTURE)

//  from src/gui/image/qpicture.cpp, line 984, as _ZN15QPicturePrivateC1ERKS_
#if !defined(QT_NO_PICTURE)
inline QPicturePrivate::QPicturePrivate(const QPicturePrivate &other)
    : pictb(&pictbData),
      trecs(other.trecs),
      formatOk(other.formatOk),
      formatMinor(other.formatMinor),
      brect(other.brect),
      override_rect(other.override_rect),
      in_memory_only(false)
{
    pictb.setData(other.pictb.data(), other.pictb.size());
    if (other.pictb.isOpen()) {
        pictb.open(other.pictb.openMode());
        pictb.seek(other.pictb.pos());
    }
}
#endif  // !defined(QT_NO_PICTURE)
//  -----------------------------------------------------------------------

//  QPicturePrivate::QPicturePrivate()
extern "C" Q_DECL_EXPORT
QPicturePrivate *ritual_ZN15QPicturePrivateC1Ev() {
  return new QPicturePrivate();
}

//  QPicturePrivate::QPicturePrivate(const QPicturePrivate &other)
extern "C" Q_DECL_EXPORT
QPicturePrivate *ritual_ZN15QPicturePrivateC1ERKS_(
    const QPicturePrivate *other) {
  return new QPicturePrivate(*other);
}

//  QPicturePrivate::~QPicturePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPicturePrivateD1Ev(QPicturePrivate *self) {
  delete self;
}
