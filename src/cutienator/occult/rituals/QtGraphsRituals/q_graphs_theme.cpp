//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qgraphstheme.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qgraphstheme.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphscolor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QGraphsTheme may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphsTheme : QGraphsTheme {
  using QGraphsTheme::classBegin;
  using QGraphsTheme::componentComplete;
};

//  A QGraphsTheme that Python can take functions over in. Every QGraphsTheme
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphsThemeCall0)(const void *, int *);
typedef void (*CuteQGraphsThemeCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphsThemeCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphsThemeCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsThemeCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsThemeCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsThemeCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsThemeCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsThemeCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphsTheme : public QGraphsTheme {
public:
  using QGraphsTheme::QGraphsTheme;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGraphsTheme::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphsThemeCall0 call = reinterpret_cast<CuteQGraphsThemeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphsTheme::classBegin();
  }

  //  void QGraphsTheme::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphsThemeCall1 call = reinterpret_cast<CuteQGraphsThemeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphsTheme::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphsThemeCall2 call = reinterpret_cast<CuteQGraphsThemeCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphsThemeCall3 call = reinterpret_cast<CuteQGraphsThemeCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphsThemeCall4 call = reinterpret_cast<CuteQGraphsThemeCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphsThemeCall5 call = reinterpret_cast<CuteQGraphsThemeCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphsThemeCall6 call = reinterpret_cast<CuteQGraphsThemeCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphsThemeCall7 call = reinterpret_cast<CuteQGraphsThemeCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphsThemeCall8 call = reinterpret_cast<CuteQGraphsThemeCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphsTheme::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QGraphsTheme10metaObjectEv(
    const QGraphsTheme *self) {
  return self->metaObject();
}

//  QString QGraphsTheme::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QGraphsTheme2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphsTheme::tr(s, c, n));
}

//  QGraphsTheme::QGraphsTheme(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_ZN12QGraphsThemeC1EP7QObject(QObject *parent) {
  return new CuteQGraphsTheme(parent);
}

//  QGraphsTheme::~QGraphsTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsThemeD1Ev(QGraphsTheme *self) {
  delete self;
}

//  bool QGraphsTheme::themeDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGraphsTheme10themeDirtyEv(const QGraphsTheme *self) {
  return self->themeDirty();
}

//  void QGraphsTheme::resetThemeDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme15resetThemeDirtyEv(QGraphsTheme *self) {
  self->resetThemeDirty();
}

//  void QGraphsTheme::resetColorTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme15resetColorThemeEv(QGraphsTheme *self) {
  self->resetColorTheme();
}

//  QGraphsThemeDirtyBitField *QGraphsTheme::dirtyBits()
extern "C" Q_DECL_EXPORT
QGraphsThemeDirtyBitField *ritual_ZN12QGraphsTheme9dirtyBitsEv(
    QGraphsTheme *self) {
  return self->dirtyBits();
}

//  void QGraphsTheme::resetDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme14resetDirtyBitsEv(QGraphsTheme *self) {
  self->resetDirtyBits();
}

//  ColorScheme QGraphsTheme::colorScheme() const
extern "C" Q_DECL_EXPORT
QGraphsTheme::ColorScheme ritual_ZNK12QGraphsTheme11colorSchemeEv(
    const QGraphsTheme *self) {
  return self->colorScheme();
}

//  void QGraphsTheme::setColorScheme(ColorScheme newColorScheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme14setColorSchemeENS_11ColorSchemeE(
    QGraphsTheme *self,
    QGraphsTheme::ColorScheme newColorScheme) {
  self->setColorScheme(newColorScheme);
}

//  Theme QGraphsTheme::theme() const
extern "C" Q_DECL_EXPORT
QGraphsTheme::Theme ritual_ZNK12QGraphsTheme5themeEv(
    const QGraphsTheme *self) {
  return self->theme();
}

//  void QGraphsTheme::setTheme(Theme newTheme, ForceTheme force)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme8setThemeENS_5ThemeENS_10ForceThemeE(
    QGraphsTheme *self,
    QGraphsTheme::Theme newTheme,
    QGraphsTheme::ForceTheme force) {
  self->setTheme(newTheme, force);
}

//  ColorStyle QGraphsTheme::colorStyle() const
extern "C" Q_DECL_EXPORT
QGraphsTheme::ColorStyle ritual_ZNK12QGraphsTheme10colorStyleEv(
    const QGraphsTheme *self) {
  return self->colorStyle();
}

//  void QGraphsTheme::setColorStyle(ColorStyle newColorStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme13setColorStyleENS_10ColorStyleE(
    QGraphsTheme *self,
    QGraphsTheme::ColorStyle newColorStyle) {
  self->setColorStyle(newColorStyle);
}

//  QColor QGraphsTheme::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QGraphsTheme15backgroundColorEv(
    const QGraphsTheme *self) {
  return new QColor(self->backgroundColor());
}

//  void QGraphsTheme::setBackgroundColor(QColor newBackgroundColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme18setBackgroundColorE6QColor(
    QGraphsTheme *self,
    const QColor *newBackgroundColor) {
  self->setBackgroundColor(*newBackgroundColor);
}

//  bool QGraphsTheme::isBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGraphsTheme19isBackgroundVisibleEv(
    const QGraphsTheme *self) {
  return self->isBackgroundVisible();
}

//  void QGraphsTheme::setBackgroundVisible(bool newBackgroundVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme20setBackgroundVisibleEb(
    QGraphsTheme *self,
    bool newBackgroundVisible) {
  self->setBackgroundVisible(newBackgroundVisible);
}

//  QColor QGraphsTheme::plotAreaBackgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QGraphsTheme23plotAreaBackgroundColorEv(
    const QGraphsTheme *self) {
  return new QColor(self->plotAreaBackgroundColor());
}

//  void QGraphsTheme::setPlotAreaBackgroundColor(QColor newBackgroundColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme26setPlotAreaBackgroundColorE6QColor(
    QGraphsTheme *self,
    const QColor *newBackgroundColor) {
  self->setPlotAreaBackgroundColor(*newBackgroundColor);
}

//  bool QGraphsTheme::isPlotAreaBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGraphsTheme27isPlotAreaBackgroundVisibleEv(
    const QGraphsTheme *self) {
  return self->isPlotAreaBackgroundVisible();
}

//  void QGraphsTheme::setPlotAreaBackgroundVisible(bool
//      newBackgroundVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme28setPlotAreaBackgroundVisibleEb(
    QGraphsTheme *self,
    bool newBackgroundVisibility) {
  self->setPlotAreaBackgroundVisible(newBackgroundVisibility);
}

//  bool QGraphsTheme::isGridVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGraphsTheme13isGridVisibleEv(const QGraphsTheme *self) {
  return self->isGridVisible();
}

//  void QGraphsTheme::setGridVisible(bool newGridVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme14setGridVisibleEb(
    QGraphsTheme *self,
    bool newGridVisibility) {
  self->setGridVisible(newGridVisibility);
}

//  bool QGraphsTheme::labelsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGraphsTheme13labelsVisibleEv(const QGraphsTheme *self) {
  return self->labelsVisible();
}

//  void QGraphsTheme::setLabelsVisible(bool newLabelsVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme16setLabelsVisibleEb(
    QGraphsTheme *self,
    bool newLabelsVisibility) {
  self->setLabelsVisible(newLabelsVisibility);
}

//  QColor QGraphsTheme::labelBackgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QGraphsTheme20labelBackgroundColorEv(
    const QGraphsTheme *self) {
  return new QColor(self->labelBackgroundColor());
}

//  void QGraphsTheme::setLabelBackgroundColor(QColor
//      newLabelBackgroundColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme23setLabelBackgroundColorE6QColor(
    QGraphsTheme *self,
    const QColor *newLabelBackgroundColor) {
  self->setLabelBackgroundColor(*newLabelBackgroundColor);
}

//  QColor QGraphsTheme::labelTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QGraphsTheme14labelTextColorEv(
    const QGraphsTheme *self) {
  return new QColor(self->labelTextColor());
}

//  void QGraphsTheme::setLabelTextColor(QColor newLabelTextColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme17setLabelTextColorE6QColor(
    QGraphsTheme *self,
    const QColor *newLabelTextColor) {
  self->setLabelTextColor(*newLabelTextColor);
}

//  QColor QGraphsTheme::singleHighlightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QGraphsTheme20singleHighlightColorEv(
    const QGraphsTheme *self) {
  return new QColor(self->singleHighlightColor());
}

//  void QGraphsTheme::setSingleHighlightColor(QColor
//      newSingleHighlightColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme23setSingleHighlightColorE6QColor(
    QGraphsTheme *self,
    const QColor *newSingleHighlightColor) {
  self->setSingleHighlightColor(*newSingleHighlightColor);
}

//  QColor QGraphsTheme::multiHighlightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK12QGraphsTheme19multiHighlightColorEv(
    const QGraphsTheme *self) {
  return new QColor(self->multiHighlightColor());
}

//  void QGraphsTheme::setMultiHighlightColor(QColor newMultiHighlightColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme22setMultiHighlightColorE6QColor(
    QGraphsTheme *self,
    const QColor *newMultiHighlightColor) {
  self->setMultiHighlightColor(*newMultiHighlightColor);
}

//  void QGraphsTheme::setSingleHighlightGradient(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme26setSingleHighlightGradientERK15QLinearGradient(
    QGraphsTheme *self,
    const QLinearGradient *gradient) {
  self->setSingleHighlightGradient(*gradient);
}

//  QLinearGradient QGraphsTheme::singleHighlightGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK12QGraphsTheme23singleHighlightGradientEv(
    const QGraphsTheme *self) {
  return new QLinearGradient(self->singleHighlightGradient());
}

//  void QGraphsTheme::setMultiHighlightGradient(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme25setMultiHighlightGradientERK15QLinearGradient(
    QGraphsTheme *self,
    const QLinearGradient *gradient) {
  self->setMultiHighlightGradient(*gradient);
}

//  QLinearGradient QGraphsTheme::multiHighlightGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK12QGraphsTheme22multiHighlightGradientEv(
    const QGraphsTheme *self) {
  return new QLinearGradient(self->multiHighlightGradient());
}

//  QFont QGraphsTheme::labelFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QGraphsTheme9labelFontEv(const QGraphsTheme *self) {
  return new QFont(self->labelFont());
}

//  void QGraphsTheme::setLabelFont(const QFont &newFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme12setLabelFontERK5QFont(
    QGraphsTheme *self,
    const QFont *newFont) {
  self->setLabelFont(*newFont);
}

//  QList<QColor> QGraphsTheme::seriesColors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK12QGraphsTheme12seriesColorsEv(
    const QGraphsTheme *self) {
  return new QList<QColor>(self->seriesColors());
}

//  void QGraphsTheme::setSeriesColors(const QList<QColor> &newSeriesColors)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme15setSeriesColorsERK5QListI6QColorE(
    QGraphsTheme *self,
    const QList<QColor> *newSeriesColors) {
  self->setSeriesColors(*newSeriesColors);
}

//  QList<QColor> QGraphsTheme::borderColors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK12QGraphsTheme12borderColorsEv(
    const QGraphsTheme *self) {
  return new QList<QColor>(self->borderColors());
}

//  void QGraphsTheme::setBorderColors(const QList<QColor> &newBorderColors)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme15setBorderColorsERK5QListI6QColorE(
    QGraphsTheme *self,
    const QList<QColor> *newBorderColors) {
  self->setBorderColors(*newBorderColors);
}

//  QList<QLinearGradient> QGraphsTheme::seriesGradients() const
extern "C" Q_DECL_EXPORT
QList<QLinearGradient> *ritual_ZNK12QGraphsTheme15seriesGradientsEv(
    const QGraphsTheme *self) {
  return new QList<QLinearGradient>(self->seriesGradients());
}

//  void QGraphsTheme::setSeriesGradients(const QList<QLinearGradient>
//      &newSeriesGradients)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme18setSeriesGradientsERK5QListI15QLinearGradientE(
    QGraphsTheme *self,
    const QList<QLinearGradient> *newSeriesGradients) {
  self->setSeriesGradients(*newSeriesGradients);
}

//  bool QGraphsTheme::isLabelBackgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGraphsTheme24isLabelBackgroundVisibleEv(
    const QGraphsTheme *self) {
  return self->isLabelBackgroundVisible();
}

//  void QGraphsTheme::setLabelBackgroundVisible(bool
//      newLabelBackgroundVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme25setLabelBackgroundVisibleEb(
    QGraphsTheme *self,
    bool newLabelBackgroundVisibility) {
  self->setLabelBackgroundVisible(newLabelBackgroundVisibility);
}

//  bool QGraphsTheme::isLabelBorderVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGraphsTheme20isLabelBorderVisibleEv(
    const QGraphsTheme *self) {
  return self->isLabelBorderVisible();
}

//  void QGraphsTheme::setLabelBorderVisible(bool newLabelBorderVisibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme21setLabelBorderVisibleEb(
    QGraphsTheme *self,
    bool newLabelBorderVisibility) {
  self->setLabelBorderVisible(newLabelBorderVisibility);
}

//  qreal QGraphsTheme::borderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QGraphsTheme11borderWidthEv(const QGraphsTheme *self) {
  return self->borderWidth();
}

//  void QGraphsTheme::setBorderWidth(qreal newBorderWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme14setBorderWidthEd(
    QGraphsTheme *self,
    qreal newBorderWidth) {
  self->setBorderWidth(newBorderWidth);
}

//  QFont QGraphsTheme::axisXLabelFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QGraphsTheme14axisXLabelFontEv(const QGraphsTheme *self) {
  return new QFont(self->axisXLabelFont());
}

//  void QGraphsTheme::setAxisXLabelFont(const QFont &newAxisXLabelFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme17setAxisXLabelFontERK5QFont(
    QGraphsTheme *self,
    const QFont *newAxisXLabelFont) {
  self->setAxisXLabelFont(*newAxisXLabelFont);
}

//  QFont QGraphsTheme::axisYLabelFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QGraphsTheme14axisYLabelFontEv(const QGraphsTheme *self) {
  return new QFont(self->axisYLabelFont());
}

//  void QGraphsTheme::setAxisYLabelFont(const QFont &newAxisYLabelFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme17setAxisYLabelFontERK5QFont(
    QGraphsTheme *self,
    const QFont *newAxisYLabelFont) {
  self->setAxisYLabelFont(*newAxisYLabelFont);
}

//  QFont QGraphsTheme::axisZLabelFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK12QGraphsTheme14axisZLabelFontEv(const QGraphsTheme *self) {
  return new QFont(self->axisZLabelFont());
}

//  void QGraphsTheme::setAxisZLabelFont(const QFont &newAxisZLabelFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme17setAxisZLabelFontERK5QFont(
    QGraphsTheme *self,
    const QFont *newAxisZLabelFont) {
  self->setAxisZLabelFont(*newAxisZLabelFont);
}

//  QGraphsLine QGraphsTheme::grid() const
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZNK12QGraphsTheme4gridEv(const QGraphsTheme *self) {
  return new QGraphsLine(self->grid());
}

//  void QGraphsTheme::setGrid(const QGraphsLine &newGrid)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme7setGridERK11QGraphsLine(
    QGraphsTheme *self,
    const QGraphsLine *newGrid) {
  self->setGrid(*newGrid);
}

//  QGraphsLine QGraphsTheme::axisX() const
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZNK12QGraphsTheme5axisXEv(const QGraphsTheme *self) {
  return new QGraphsLine(self->axisX());
}

//  void QGraphsTheme::setAxisX(const QGraphsLine &newAxisX)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme8setAxisXERK11QGraphsLine(
    QGraphsTheme *self,
    const QGraphsLine *newAxisX) {
  self->setAxisX(*newAxisX);
}

//  QGraphsLine QGraphsTheme::axisY() const
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZNK12QGraphsTheme5axisYEv(const QGraphsTheme *self) {
  return new QGraphsLine(self->axisY());
}

//  void QGraphsTheme::setAxisY(const QGraphsLine &newAxisY)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme8setAxisYERK11QGraphsLine(
    QGraphsTheme *self,
    const QGraphsLine *newAxisY) {
  self->setAxisY(*newAxisY);
}

//  QGraphsLine QGraphsTheme::axisZ() const
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZNK12QGraphsTheme5axisZEv(const QGraphsTheme *self) {
  return new QGraphsLine(self->axisZ());
}

//  void QGraphsTheme::setAxisZ(const QGraphsLine &newAxisZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme8setAxisZERK11QGraphsLine(
    QGraphsTheme *self,
    const QGraphsLine *newAxisZ) {
  self->setAxisZ(*newAxisZ);
}

//  void QGraphsTheme::handleBaseColorUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme21handleBaseColorUpdateEv(QGraphsTheme *self) {
  self->handleBaseColorUpdate();
}

//  void QGraphsTheme::handleBaseGradientUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme24handleBaseGradientUpdateEv(
    QGraphsTheme *self) {
  self->handleBaseGradientUpdate();
}

//  void QGraphsTheme::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme10classBeginEv(QGraphsTheme *self) {
  self->classBegin();
}

//  void QGraphsTheme::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme17componentCompleteEv(QGraphsTheme *self) {
  self->componentComplete();
}

//  void QGraphsTheme::updateAutomaticColorScheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme26updateAutomaticColorSchemeEv(
    QGraphsTheme *self) {
  self->updateAutomaticColorScheme();
}

//  void QGraphsTheme::setColorSchemePalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme21setColorSchemePaletteEv(QGraphsTheme *self) {
  self->setColorSchemePalette();
}

//  void QGraphsTheme::setThemePalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme15setThemePaletteEv(QGraphsTheme *self) {
  self->setThemePalette();
}

//  QLinearGradient QGraphsTheme::createGradient(QColor color, float
//      colorLevel)
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZN12QGraphsTheme14createGradientE6QColorf(
    QGraphsTheme *self,
    const QColor *color,
    float colorLevel) {
  return new QLinearGradient(self->createGradient(*color, colorLevel));
}

//  void QGraphsTheme::setThemeGradient(QQuickGradient *gradient,
//      GradientQMLStyle type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme16setThemeGradientEP14QQuickGradientNS_16GradientQMLStyleE(
    QGraphsTheme *self,
    QQuickGradient *gradient,
    QGraphsTheme::GradientQMLStyle type) {
  self->setThemeGradient(gradient, type);
}

//  QLinearGradient QGraphsTheme::convertGradient(QQuickGradient *gradient)
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZN12QGraphsTheme15convertGradientEP14QQuickGradient(
    QGraphsTheme *self,
    QQuickGradient *gradient) {
  return new QLinearGradient(self->convertGradient(gradient));
}

//  void QGraphsTheme::addColor(QQuickGraphsColor *color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme8addColorEP17QQuickGraphsColor(
    QGraphsTheme *self,
    QQuickGraphsColor *color) {
  self->addColor(color);
}

//  QList<QQuickGraphsColor *> QGraphsTheme::colorList()
extern "C" Q_DECL_EXPORT
QList<QQuickGraphsColor *> *ritual_ZN12QGraphsTheme9colorListEv(
    QGraphsTheme *self) {
  return new QList<QQuickGraphsColor *>(self->colorList());
}

//  void QGraphsTheme::clearColors()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme11clearColorsEv(QGraphsTheme *self) {
  self->clearColors();
}

//  void QGraphsTheme::clearDummyColors()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme16clearDummyColorsEv(QGraphsTheme *self) {
  self->clearDummyColors();
}

//  void QGraphsTheme::clearGradients()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme14clearGradientsEv(QGraphsTheme *self) {
  self->clearGradients();
}

//  QList<QQuickGradient *> QGraphsTheme::gradientList()
extern "C" Q_DECL_EXPORT
QList<QQuickGradient *> *ritual_ZN12QGraphsTheme12gradientListEv(
    QGraphsTheme *self) {
  return new QList<QQuickGradient *>(self->gradientList());
}

//  void QGraphsTheme::addGradient(QQuickGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme11addGradientEP14QQuickGradient(
    QGraphsTheme *self,
    QQuickGradient *gradient) {
  self->addGradient(gradient);
}

//  void QGraphsTheme::setSingleHighlightGradientQML(QQuickGradient
//      *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme29setSingleHighlightGradientQMLEP14QQuickGradient(
    QGraphsTheme *self,
    QQuickGradient *gradient) {
  self->setSingleHighlightGradientQML(gradient);
}

//  QQuickGradient *QGraphsTheme::singleHighlightGradientQML() const
extern "C" Q_DECL_EXPORT
QQuickGradient *ritual_ZNK12QGraphsTheme26singleHighlightGradientQMLEv(
    const QGraphsTheme *self) {
  return self->singleHighlightGradientQML();
}

//  void QGraphsTheme::setMultiHighlightGradientQML(QQuickGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGraphsTheme28setMultiHighlightGradientQMLEP14QQuickGradient(
    QGraphsTheme *self,
    QQuickGradient *gradient) {
  self->setMultiHighlightGradientQML(gradient);
}

//  QQuickGradient *QGraphsTheme::multiHighlightGradientQML() const
extern "C" Q_DECL_EXPORT
QQuickGradient *ritual_ZNK12QGraphsTheme25multiHighlightGradientQMLEv(
    const QGraphsTheme *self) {
  return self->multiHighlightGradientQML();
}

//  QGraphsThemePrivate *QGraphsTheme::d_func()
extern "C" Q_DECL_EXPORT
QGraphsThemePrivate *ritual_ZN12QGraphsTheme6d_funcEv(QGraphsTheme *self) {
  return self->d_func();
}

//  const QGraphsThemePrivate *QGraphsTheme::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphsThemePrivate *ritual_ZNK12QGraphsTheme6d_funcEv(
    const QGraphsTheme *self) {
  return self->d_func();
}

//  QGraphsTheme as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QGraphsTheme_QQmlParserStatus(
    QGraphsTheme *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQGraphsTheme, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphsTheme(
    QGraphsTheme *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphsTheme *>(self)->take(key, call);
}

//  void QGraphsTheme::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGraphsTheme10classBeginEv(QGraphsTheme *self) {
  static_cast<OwnQGraphsTheme *>(self)->OwnQGraphsTheme::classBegin();
}

//  void QGraphsTheme::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QGraphsTheme17componentCompleteEv(QGraphsTheme *self) {
  static_cast<OwnQGraphsTheme *>(self)->OwnQGraphsTheme::componentComplete();
}

//  QList<QGraphsTheme *>::QList()
extern "C" Q_DECL_EXPORT
QList<QGraphsTheme *> *ritual_list_make_QGraphsTheme_ptr() {
  return new QList<QGraphsTheme *>();
}

//  void QList<QGraphsTheme *>::append(const QGraphsTheme * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGraphsTheme_ptr(
    QList<QGraphsTheme *> *self,
    QGraphsTheme *element) {
  self->append(element);
}

//  qsizetype QList<QGraphsTheme *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGraphsTheme_ptr(
    const QList<QGraphsTheme *> *self) {
  return self->size();
}

//  const QGraphsTheme * &QList<QGraphsTheme *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_list_at_QGraphsTheme_ptr(
    const QList<QGraphsTheme *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QGraphsTheme *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGraphsTheme_ptr(QList<QGraphsTheme *> *self) {
  delete self;
}
