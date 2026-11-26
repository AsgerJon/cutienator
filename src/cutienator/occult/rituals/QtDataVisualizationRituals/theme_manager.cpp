//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/thememanager_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/thememanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/q3dtheme.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/thememanager_p.h>
#include <QtDataVisualization/private/q3dtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 10, as local:thememanager.cpp:defaultColorLevel
const float defaultColorLevel = 0.5f;

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 18, as _ZN12ThemeManagerD1Ev
inline ThemeManager::~ThemeManager()
{
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 85, as _ZNK12ThemeManager11activeThemeEv
inline Q3DTheme *ThemeManager::activeTheme() const
{
    return m_activeTheme;
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 90, as _ZNK12ThemeManager6themesEv
inline QList<Q3DTheme *> ThemeManager::themes() const
{
    return m_themes;
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 95, as _ZN12ThemeManager19connectThemeSignalsEv
inline void ThemeManager::connectThemeSignals()
{
    connect(m_activeTheme, &Q3DTheme::colorStyleChanged,
            m_controller, &Abstract3DController::handleThemeColorStyleChanged);
    connect(m_activeTheme, &Q3DTheme::baseColorsChanged,
            m_controller, &Abstract3DController::handleThemeBaseColorsChanged);
    connect(m_activeTheme, &Q3DTheme::singleHighlightColorChanged,
            m_controller, &Abstract3DController::handleThemeSingleHighlightColorChanged);
    connect(m_activeTheme, &Q3DTheme::multiHighlightColorChanged,
            m_controller, &Abstract3DController::handleThemeMultiHighlightColorChanged);
    connect(m_activeTheme, &Q3DTheme::baseGradientsChanged,
            m_controller, &Abstract3DController::handleThemeBaseGradientsChanged);
    connect(m_activeTheme, &Q3DTheme::singleHighlightGradientChanged,
            m_controller, &Abstract3DController::handleThemeSingleHighlightGradientChanged);
    connect(m_activeTheme, &Q3DTheme::multiHighlightGradientChanged,
            m_controller, &Abstract3DController::handleThemeMultiHighlightGradientChanged);
    connect(m_activeTheme, &Q3DTheme::typeChanged,
            m_controller, &Abstract3DController::handleThemeTypeChanged);

    connect(m_activeTheme->d_ptr.data(), &Q3DThemePrivate::needRender,
            m_controller, &Abstract3DController::needRender);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 439, as _ZN12ThemeManager14createGradientERK6QColorf
inline QLinearGradient ThemeManager::createGradient(const QColor &color, float colorLevel)
{
    QColor startColor;
    QLinearGradient gradient = QLinearGradient(qreal(gradientTextureWidth),
                                               qreal(gradientTextureHeight),
                                               0.0, 0.0);;
    startColor.setRed(color.red() * colorLevel);
    startColor.setGreen(color.green() * colorLevel);
    startColor.setBlue(color.blue() * colorLevel);
    gradient.setColorAt(0.0, startColor);
    gradient.setColorAt(1.0, color);
    return gradient;
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 453, as _ZN12ThemeManager13setBaseColorsEP8Q3DThemeRK5QListI6QColorE
inline void ThemeManager::setBaseColors(Q3DTheme *theme, const QList<QColor> &colors)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.baseColorDirty)
        theme->setBaseColors(colors);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 459, as _ZN12ThemeManager18setBackgroundColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setBackgroundColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.backgroundColorDirty)
        theme->setBackgroundColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 465, as _ZN12ThemeManager14setWindowColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setWindowColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.windowColorDirty)
        theme->setWindowColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 471, as _ZN12ThemeManager12setTextColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setTextColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.labelTextColorDirty)
        theme->setLabelTextColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 477, as _ZN12ThemeManager22setTextBackgroundColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setTextBackgroundColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.labelBackgroundColorDirty)
        theme->setLabelBackgroundColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 483, as _ZN12ThemeManager16setGridLineColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setGridLineColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.gridLineColorDirty)
        theme->setGridLineColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 489, as _ZN12ThemeManager23setSingleHighlightColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setSingleHighlightColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.singleHighlightColorDirty)
        theme->setSingleHighlightColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 495, as _ZN12ThemeManager22setMultiHighlightColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setMultiHighlightColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.multiHighlightColorDirty)
        theme->setMultiHighlightColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 501, as _ZN12ThemeManager13setLightColorEP8Q3DThemeRK6QColor
inline void ThemeManager::setLightColor(Q3DTheme *theme, const QColor &color)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.lightColorDirty)
        theme->setLightColor(color);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 507, as _ZN12ThemeManager16setBaseGradientsEP8Q3DThemeRK5QListI15QLinearGradientE
inline void ThemeManager::setBaseGradients(Q3DTheme *theme, const QList<QLinearGradient> &gradients)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.baseGradientDirty)
        theme->setBaseGradients(gradients);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 513, as _ZN12ThemeManager26setSingleHighlightGradientEP8Q3DThemeRK15QLinearGradient
inline void ThemeManager::setSingleHighlightGradient(Q3DTheme *theme, const QLinearGradient &gradient)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.singleHighlightGradientDirty)
        theme->setSingleHighlightGradient(gradient);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 519, as _ZN12ThemeManager25setMultiHighlightGradientEP8Q3DThemeRK15QLinearGradient
inline void ThemeManager::setMultiHighlightGradient(Q3DTheme *theme, const QLinearGradient &gradient)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.multiHighlightGradientDirty)
        theme->setMultiHighlightGradient(gradient);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 525, as _ZN12ThemeManager16setLightStrengthEP8Q3DThemef
inline void ThemeManager::setLightStrength(Q3DTheme *theme, float strength)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.lightStrengthDirty)
        theme->setLightStrength(strength);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 531, as _ZN12ThemeManager23setAmbientLightStrengthEP8Q3DThemef
inline void ThemeManager::setAmbientLightStrength(Q3DTheme *theme, float strength)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.ambientLightStrengthDirty)
        theme->setAmbientLightStrength(strength);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 537, as _ZN12ThemeManager25setHighlightLightStrengthEP8Q3DThemef
inline void ThemeManager::setHighlightLightStrength(Q3DTheme *theme, float strength)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.highlightLightStrengthDirty)
        theme->setHighlightLightStrength(strength);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 543, as _ZN12ThemeManager21setLabelBorderEnabledEP8Q3DThemeb
inline void ThemeManager::setLabelBorderEnabled(Q3DTheme *theme, bool enabled)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.labelBorderEnabledDirty)
        theme->setLabelBorderEnabled(enabled);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 549, as _ZN12ThemeManager7setFontEP8Q3DThemeRK5QFont
inline void ThemeManager::setFont(Q3DTheme *theme, const QFont &font)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.fontDirty)
        theme->setFont(font);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 555, as _ZN12ThemeManager20setBackgroundEnabledEP8Q3DThemeb
inline void ThemeManager::setBackgroundEnabled(Q3DTheme *theme, bool enabled)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.backgroundEnabledDirty)
        theme->setBackgroundEnabled(enabled);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 561, as _ZN12ThemeManager14setGridEnabledEP8Q3DThemeb
inline void ThemeManager::setGridEnabled(Q3DTheme *theme, bool enabled)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.gridEnabledDirty)
        theme->setGridEnabled(enabled);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 567, as _ZN12ThemeManager25setLabelBackgroundEnabledEP8Q3DThemeb
inline void ThemeManager::setLabelBackgroundEnabled(Q3DTheme *theme, bool enabled)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.labelBackgroundEnabledDirty)
        theme->setLabelBackgroundEnabled(enabled);
}

//  from ../qtdatavis3d/src/datavisualization/theme/thememanager.cpp, line 573, as _ZN12ThemeManager13setColorStyleEP8Q3DThemeNS0_10ColorStyleE
inline void ThemeManager::setColorStyle(Q3DTheme *theme, Q3DTheme::ColorStyle style)
{
    if (theme->d_ptr->isForcePredefinedType() || !theme->d_ptr->m_dirtyBits.colorStyleDirty)
        theme->setColorStyle(style);
}
//  -----------------------------------------------------------------------

//  A ThemeManager that Python can take functions over in. Every ThemeManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteThemeManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteThemeManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteThemeManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteThemeManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteThemeManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteThemeManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteThemeManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteThemeManager : public ThemeManager {
public:
  using ThemeManager::ThemeManager;
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
      CuteThemeManagerCall0 call = reinterpret_cast<CuteThemeManagerCall0>(taken[0]);
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
      CuteThemeManagerCall1 call = reinterpret_cast<CuteThemeManagerCall1>(taken[1]);
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
      CuteThemeManagerCall2 call = reinterpret_cast<CuteThemeManagerCall2>(taken[2]);
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
      CuteThemeManagerCall3 call = reinterpret_cast<CuteThemeManagerCall3>(taken[3]);
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
      CuteThemeManagerCall4 call = reinterpret_cast<CuteThemeManagerCall4>(taken[4]);
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
      CuteThemeManagerCall5 call = reinterpret_cast<CuteThemeManagerCall5>(taken[5]);
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
      CuteThemeManagerCall6 call = reinterpret_cast<CuteThemeManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ThemeManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12ThemeManager10metaObjectEv(
    const ThemeManager *self) {
  return self->metaObject();
}

//  void *ThemeManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12ThemeManager11qt_metacastEPKc(
    ThemeManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ThemeManager::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12ThemeManager11qt_metacallEN11QMetaObject4CallEiPPv(
    ThemeManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  ThemeManager::~ThemeManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManagerD1Ev(ThemeManager *self) {
  delete self;
}

//  Q3DTheme *ThemeManager::activeTheme() const
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZNK12ThemeManager11activeThemeEv(const ThemeManager *self) {
  return self->activeTheme();
}

//  QList<Q3DTheme *> ThemeManager::themes() const
extern "C" Q_DECL_EXPORT
QList<Q3DTheme *> *ritual_ZNK12ThemeManager6themesEv(
    const ThemeManager *self) {
  return new QList<Q3DTheme *>(self->themes());
}

//  void ThemeManager::connectThemeSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager19connectThemeSignalsEv(ThemeManager *self) {
  self->connectThemeSignals();
}

//  QLinearGradient ThemeManager::createGradient(const QColor &color, float
//      colorLevel)
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZN12ThemeManager14createGradientERK6QColorf(
    const QColor *color,
    float colorLevel) {
  return new QLinearGradient(
      ThemeManager::createGradient(
          *color,
          colorLevel));
}

//  void ThemeManager::setBaseColors(Q3DTheme *theme, const QList<QColor>
//      &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager13setBaseColorsEP8Q3DThemeRK5QListI6QColorE(
    Q3DTheme *theme,
    const QList<QColor> *colors) {
  ThemeManager::setBaseColors(theme, *colors);
}

//  void ThemeManager::setBackgroundColor(Q3DTheme *theme, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager18setBackgroundColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setBackgroundColor(theme, *color);
}

//  void ThemeManager::setWindowColor(Q3DTheme *theme, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager14setWindowColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setWindowColor(theme, *color);
}

//  void ThemeManager::setTextColor(Q3DTheme *theme, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager12setTextColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setTextColor(theme, *color);
}

//  void ThemeManager::setTextBackgroundColor(Q3DTheme *theme, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager22setTextBackgroundColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setTextBackgroundColor(theme, *color);
}

//  void ThemeManager::setGridLineColor(Q3DTheme *theme, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager16setGridLineColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setGridLineColor(theme, *color);
}

//  void ThemeManager::setSingleHighlightColor(Q3DTheme *theme, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager23setSingleHighlightColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setSingleHighlightColor(theme, *color);
}

//  void ThemeManager::setMultiHighlightColor(Q3DTheme *theme, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager22setMultiHighlightColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setMultiHighlightColor(theme, *color);
}

//  void ThemeManager::setLightColor(Q3DTheme *theme, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager13setLightColorEP8Q3DThemeRK6QColor(
    Q3DTheme *theme,
    const QColor *color) {
  ThemeManager::setLightColor(theme, *color);
}

//  void ThemeManager::setBaseGradients(Q3DTheme *theme, const
//      QList<QLinearGradient> &gradients)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager16setBaseGradientsEP8Q3DThemeRK5QListI15QLinearGradientE(
    Q3DTheme *theme,
    const QList<QLinearGradient> *gradients) {
  ThemeManager::setBaseGradients(theme, *gradients);
}

//  void ThemeManager::setSingleHighlightGradient(Q3DTheme *theme, const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager26setSingleHighlightGradientEP8Q3DThemeRK15QLinearGradient(
    Q3DTheme *theme,
    const QLinearGradient *gradient) {
  ThemeManager::setSingleHighlightGradient(theme, *gradient);
}

//  void ThemeManager::setMultiHighlightGradient(Q3DTheme *theme, const
//      QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager25setMultiHighlightGradientEP8Q3DThemeRK15QLinearGradient(
    Q3DTheme *theme,
    const QLinearGradient *gradient) {
  ThemeManager::setMultiHighlightGradient(theme, *gradient);
}

//  void ThemeManager::setLightStrength(Q3DTheme *theme, float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager16setLightStrengthEP8Q3DThemef(
    Q3DTheme *theme,
    float strength) {
  ThemeManager::setLightStrength(theme, strength);
}

//  void ThemeManager::setAmbientLightStrength(Q3DTheme *theme, float
//      strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager23setAmbientLightStrengthEP8Q3DThemef(
    Q3DTheme *theme,
    float strength) {
  ThemeManager::setAmbientLightStrength(theme, strength);
}

//  void ThemeManager::setHighlightLightStrength(Q3DTheme *theme, float
//      strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager25setHighlightLightStrengthEP8Q3DThemef(
    Q3DTheme *theme,
    float strength) {
  ThemeManager::setHighlightLightStrength(theme, strength);
}

//  void ThemeManager::setLabelBorderEnabled(Q3DTheme *theme, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager21setLabelBorderEnabledEP8Q3DThemeb(
    Q3DTheme *theme,
    bool enabled) {
  ThemeManager::setLabelBorderEnabled(theme, enabled);
}

//  void ThemeManager::setFont(Q3DTheme *theme, const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager7setFontEP8Q3DThemeRK5QFont(
    Q3DTheme *theme,
    const QFont *font) {
  ThemeManager::setFont(theme, *font);
}

//  void ThemeManager::setBackgroundEnabled(Q3DTheme *theme, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager20setBackgroundEnabledEP8Q3DThemeb(
    Q3DTheme *theme,
    bool enabled) {
  ThemeManager::setBackgroundEnabled(theme, enabled);
}

//  void ThemeManager::setGridEnabled(Q3DTheme *theme, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager14setGridEnabledEP8Q3DThemeb(
    Q3DTheme *theme,
    bool enabled) {
  ThemeManager::setGridEnabled(theme, enabled);
}

//  void ThemeManager::setLabelBackgroundEnabled(Q3DTheme *theme, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager25setLabelBackgroundEnabledEP8Q3DThemeb(
    Q3DTheme *theme,
    bool enabled) {
  ThemeManager::setLabelBackgroundEnabled(theme, enabled);
}

//  void ThemeManager::setColorStyle(Q3DTheme *theme, Q3DTheme::ColorStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ThemeManager13setColorStyleEP8Q3DThemeNS0_10ColorStyleE(
    Q3DTheme *theme,
    Q3DTheme::ColorStyle style) {
  ThemeManager::setColorStyle(theme, style);
}

//  a Python function taken by a CuteThemeManager, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ThemeManager(
    ThemeManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteThemeManager *>(self)->take(key, call);
}
