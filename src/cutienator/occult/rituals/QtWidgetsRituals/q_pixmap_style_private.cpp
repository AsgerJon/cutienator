//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qpixmapstyle_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qpixmapstyle_p.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qpixmapstyle_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qpixmapstyle_p.h"
#include "qpixmapstyle_p_p.h"
#include <QDebug>
#if QT_CONFIG(textedit)
#include <QTextEdit>
#endif
#include <QStringBuilder>
#include <QPainter>
#include <QPixmapCache>
#include <QStyleOption>
#include <QString>
#if QT_CONFIG(progressbar)
#include <QProgressBar>
#endif
#if QT_CONFIG(slider)
#include <QSlider>
#endif
#include <QEvent>
#if QT_CONFIG(combobox)
#include <QComboBox>
#endif
#if QT_CONFIG(itemviews)
#include <QAbstractItemView>
#include <QStyledItemDelegate>
#endif
#if QT_CONFIG(listview)
#include <QListView>
#endif
#include <QAbstractScrollArea>
#if QT_CONFIG(scrollbar)
#include <QScrollBar>
#endif
#if QT_CONFIG(scroller)
#include <qscroller.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/styles/qpixmapstyle.cpp, line 1153, as _ZN19QPixmapStylePrivate5scaleEiiRK7QPixmapRK22QPixmapStyleDescriptor
inline QPixmap QPixmapStylePrivate::scale(int w, int h, const QPixmap &pixmap, const QPixmapStyleDescriptor &desc)
{
    QPixmap result(w, h);
    {
        const QColor transparent(0, 0, 0, 0);
        result.fill( transparent );
        QPainter p( &result );
        const QMargins margins = desc.margins;
        qDrawBorderPixmap(&p, result.rect(), margins, pixmap,
                          pixmap.rect(), margins, desc.tileRules);
    }
    return result;
}

//  from src/widgets/styles/qpixmapstyle.cpp, line 1167, as _ZNK19QPixmapStylePrivate15getCachedPixmapEN12QPixmapStyle17ControlDescriptorERK22QPixmapStyleDescriptorRK5QSize
inline QPixmap QPixmapStylePrivate::getCachedPixmap(QPixmapStyle::ControlDescriptor control,
                                             const QPixmapStyleDescriptor &desc,
                                             const QSize &size) const
{
    Q_Q(const QPixmapStyle);

    const QString sizeString = QString::number(size.width()) % u'*'
            % QString::number(size.height());
    const QString key = QLatin1StringView(q->metaObject()->className()) % QString::number(control)
            % u'@' % sizeString;

    QPixmap result;

    if (!QPixmapCache::find( key, &result)) {
        QPixmap source(desc.fileName);
        result = scale(size.width(), size.height(), source, desc);
        QPixmapCache::insert(key, result);
    }
    return result;
}

//  from src/widgets/styles/qpixmapstyle.cpp, line 1188, as _ZNK19QPixmapStylePrivate11computeSizeERK22QPixmapStyleDescriptorii
inline QSize QPixmapStylePrivate::computeSize(const QPixmapStyleDescriptor &desc, int width, int height) const
{
    if (desc.tileRules.horizontal != Qt::RepeatTile)
        width = qMax(width, desc.size.width());
    if (desc.tileRules.vertical != Qt::RepeatTile)
        height = qMax(height, desc.size.height());
    return QSize(width, height);
}
//  -----------------------------------------------------------------------

//  A QPixmapStylePrivate that Python can take functions over in. Every QPixmapStylePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(tabbar)
typedef void (*CuteQPixmapStylePrivateCall0)(const void *, const QStyleOptionTab *, const QWidget *, QRect *, QRect *, int *);
#endif  // QT_CONFIG(tabbar)
class CuteQPixmapStylePrivate : public QPixmapStylePrivate {
public:
  using QPixmapStylePrivate::QPixmapStylePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK19QCommonStylePrivate9tabLayoutEPK15QStyleOptionTabPK7QWidgetP5QRectS7_")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
    return false;
  }

#if QT_CONFIG(tabbar)
  //  void QCommonStylePrivate::tabLayout(const QStyleOptionTab *opt, const
  //      QWidget *widget, QRect *textRect, QRect *pixmapRect) const
  void tabLayout(
      const QStyleOptionTab *opt,
      const QWidget *widget,
      QRect *textRect,
      QRect *pixmapRect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapStylePrivateCall0 call = reinterpret_cast<CuteQPixmapStylePrivateCall0>(taken[0]);
      call(this, opt, widget, textRect, pixmapRect, &handled);
      if (handled) return;
    }
    QCommonStylePrivate::tabLayout(opt, widget, textRect, pixmapRect);
  }
#endif  // QT_CONFIG(tabbar)
};

//  QPixmapStyle *QPixmapStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPixmapStyle *ritual_ZN19QPixmapStylePrivate6q_funcEv(
    QPixmapStylePrivate *self) {
  return self->q_func();
}

//  const QPixmapStyle *QPixmapStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPixmapStyle *ritual_ZNK19QPixmapStylePrivate6q_funcEv(
    const QPixmapStylePrivate *self) {
  return self->q_func();
}

//  QPixmap QPixmapStylePrivate::scale(int w, int h, const QPixmap &pixmap,
//      const QPixmapStyleDescriptor &desc)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN19QPixmapStylePrivate5scaleEiiRK7QPixmapRK22QPixmapStyleDescriptor(
    int w,
    int h,
    const QPixmap *pixmap,
    const QPixmapStyleDescriptor *desc) {
  return new QPixmap(QPixmapStylePrivate::scale(w, h, *pixmap, *desc));
}

//  QPixmap
//      QPixmapStylePrivate::getCachedPixmap(QPixmapStyle::ControlDescriptor
//      control, const QPixmapStyleDescriptor &desc, const QSize &size) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK19QPixmapStylePrivate15getCachedPixmapEN12QPixmapStyle17ControlDescriptorERK22QPixmapStyleDescriptorRK5QSize(
    const QPixmapStylePrivate *self,
    QPixmapStyle::ControlDescriptor control,
    const QPixmapStyleDescriptor *desc,
    const QSize *size) {
  return new QPixmap(self->getCachedPixmap(control, *desc, *size));
}

//  QSize QPixmapStylePrivate::computeSize(const QPixmapStyleDescriptor
//      &desc, int width, int height) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QPixmapStylePrivate11computeSizeERK22QPixmapStyleDescriptorii(
    const QPixmapStylePrivate *self,
    const QPixmapStyleDescriptor *desc,
    int width,
    int height) {
  return new QSize(self->computeSize(*desc, width, height));
}

//  a Python function taken by a CuteQPixmapStylePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapStylePrivate(
    QPixmapStylePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapStylePrivate *>(self)->take(key, call);
}
