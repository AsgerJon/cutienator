//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcommonstyle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qcommonstyle.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcommonstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qtextoption.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtWidgets/qstyleoption.h>
#include <cstring>

//  A QCommonStylePrivate that Python can take functions over in. Every QCommonStylePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(tabbar)
typedef void (*CuteQCommonStylePrivateCall0)(const void *, const QStyleOptionTab *, const QWidget *, QRect *, QRect *, int *);
#endif  // QT_CONFIG(tabbar)
class CuteQCommonStylePrivate : public QCommonStylePrivate {
public:
  using QCommonStylePrivate::QCommonStylePrivate;
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
      CuteQCommonStylePrivateCall0 call = reinterpret_cast<CuteQCommonStylePrivateCall0>(taken[0]);
      call(this, opt, widget, textRect, pixmapRect, &handled);
      if (handled) return;
    }
    QCommonStylePrivate::tabLayout(opt, widget, textRect, pixmapRect);
  }
#endif  // QT_CONFIG(tabbar)
};

//  QCommonStyle *QCommonStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QCommonStyle *ritual_ZN19QCommonStylePrivate6q_funcEv(
    QCommonStylePrivate *self) {
  return self->q_func();
}

//  const QCommonStyle *QCommonStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCommonStyle *ritual_ZNK19QCommonStylePrivate6q_funcEv(
    const QCommonStylePrivate *self) {
  return self->q_func();
}

//  QCommonStylePrivate::QCommonStylePrivate()
extern "C" Q_DECL_EXPORT
QCommonStylePrivate *ritual_ZN19QCommonStylePrivateC1Ev() {
  return new CuteQCommonStylePrivate();
}

//  QCommonStylePrivate::~QCommonStylePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonStylePrivateD1Ev(QCommonStylePrivate *self) {
  delete self;
}

//  QString QCommonStylePrivate::calculateElidedText(const QString &text,
//      const QTextOption &textOption, const QFont &font, const QRect
//      &textRect, const Qt::Alignment valign, Qt::TextElideMode
//      textElideMode, int flags, bool lastVisibleLineShouldBeElided, QPointF
//      *paintStartPosition) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QCommonStylePrivate19calculateElidedTextERK7QStringRK11QTextOptionRK5QFontRK5QRect6QFlagsIN2Qt13AlignmentFlagEENSD_13TextElideModeEibP7QPointF(
    const QCommonStylePrivate *self,
    const QString *text,
    const QTextOption *textOption,
    const QFont *font,
    const QRect *textRect,
    int valign,
    Qt::TextElideMode textElideMode,
    int flags,
    bool lastVisibleLineShouldBeElided,
    QPointF *paintStartPosition) {
  return new QString(
      self->calculateElidedText(
          *text,
          *textOption,
          *font,
          *textRect,
          QFlags<Qt::AlignmentFlag>::fromInt(valign),
          textElideMode,
          flags,
          lastVisibleLineShouldBeElided,
          paintStartPosition));
}

#if QT_CONFIG(itemviews)
//  void QCommonStylePrivate::viewItemDrawText(QPainter *p, const
//      QStyleOptionViewItem *option, const QRect &rect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCommonStylePrivate16viewItemDrawTextEP8QPainterPK20QStyleOptionViewItemRK5QRect(
    const QCommonStylePrivate *self,
    QPainter *p,
    const QStyleOptionViewItem *option,
    const QRect *rect) {
  self->viewItemDrawText(p, option, *rect);
}
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
//  void QCommonStylePrivate::viewItemLayout(const QStyleOptionViewItem *opt,
//      QRect *checkRect, QRect *pixmapRect, QRect *textRect, bool sizehint)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCommonStylePrivate14viewItemLayoutEPK20QStyleOptionViewItemP5QRectS4_S4_b(
    const QCommonStylePrivate *self,
    const QStyleOptionViewItem *opt,
    QRect *checkRect,
    QRect *pixmapRect,
    QRect *textRect,
    bool sizehint) {
  self->viewItemLayout(opt, checkRect, pixmapRect, textRect, sizehint);
}
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
//  QSize QCommonStylePrivate::viewItemSize(const QStyleOptionViewItem
//      *option, int role) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QCommonStylePrivate12viewItemSizeEPK20QStyleOptionViewItemi(
    const QCommonStylePrivate *self,
    const QStyleOptionViewItem *option,
    int role) {
  return new QSize(self->viewItemSize(option, role));
}
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
//  bool QCommonStylePrivate::isViewItemCached(const QStyleOptionViewItem
//      &option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCommonStylePrivate16isViewItemCachedERK20QStyleOptionViewItem(
    const QCommonStylePrivate *self,
    const QStyleOptionViewItem *option) {
  return self->isViewItemCached(*option);
}
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(toolbutton)
//  QString QCommonStylePrivate::toolButtonElideText(const
//      QStyleOptionToolButton *toolbutton, const QRect &textRect, int flags)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QCommonStylePrivate19toolButtonElideTextEPK22QStyleOptionToolButtonRK5QRecti(
    const QCommonStylePrivate *self,
    const QStyleOptionToolButton *toolbutton,
    const QRect *textRect,
    int flags) {
  return new QString(
      self->toolButtonElideText(
          toolbutton,
          *textRect,
          flags));
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(tabbar)
//  void QCommonStylePrivate::tabLayout(const QStyleOptionTab *opt, const
//      QWidget *widget, QRect *textRect, QRect *pixmapRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCommonStylePrivate9tabLayoutEPK15QStyleOptionTabPK7QWidgetP5QRectS7_(
    const QCommonStylePrivate *self,
    const QStyleOptionTab *opt,
    const QWidget *widget,
    QRect *textRect,
    QRect *pixmapRect) {
  self->tabLayout(opt, widget, textRect, pixmapRect);
}
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(animation)
//  QStyleAnimation *QCommonStylePrivate::animation(const QObject *target)
//      const
extern "C" Q_DECL_EXPORT
QStyleAnimation *ritual_ZNK19QCommonStylePrivate9animationEPK7QObject(
    const QCommonStylePrivate *self,
    const QObject *target) {
  return self->animation(target);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QCommonStylePrivate::startAnimation(QStyleAnimation *animation)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCommonStylePrivate14startAnimationEP15QStyleAnimation(
    const QCommonStylePrivate *self,
    QStyleAnimation *animation) {
  self->startAnimation(animation);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QCommonStylePrivate::stopAnimation(const QObject *target) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCommonStylePrivate13stopAnimationEPK7QObject(
    const QCommonStylePrivate *self,
    const QObject *target) {
  self->stopAnimation(target);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QCommonStylePrivate::removeAnimation(const QObject *target) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCommonStylePrivate15removeAnimationEPK7QObject(
    const QCommonStylePrivate *self,
    const QObject *target) {
  self->removeAnimation(target);
}
#endif  // QT_CONFIG(animation)

//  bool QCommonStylePrivate::rtl(const QStyleOption *option)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QCommonStylePrivate3rtlEPK12QStyleOption(
    const QStyleOption *option) {
  return QCommonStylePrivate::rtl(option);
}

//  a Python function taken by a CuteQCommonStylePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCommonStylePrivate(
    QCommonStylePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCommonStylePrivate *>(self)->take(key, call);
}

#if QT_CONFIG(tabbar)
//  void QCommonStylePrivate::tabLayout(const QStyleOptionTab *opt, const
//      QWidget *widget, QRect *textRect, QRect *pixmapRect) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QCommonStylePrivate9tabLayoutEPK15QStyleOptionTabPK7QWidgetP5QRectS7_(
    const QCommonStylePrivate *self,
    const QStyleOptionTab *opt,
    const QWidget *widget,
    QRect *textRect,
    QRect *pixmapRect) {
  self->QCommonStylePrivate::tabLayout(opt, widget, textRect, pixmapRect);
}
#endif  // QT_CONFIG(tabbar)
