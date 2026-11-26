//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dtheme.h, Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/q3dtheme.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Q3DTheme that Python can take functions over in. Every Q3DTheme
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DThemeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DThemeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DTheme : public Q3DTheme {
public:
  using Q3DTheme::Q3DTheme;
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
      CuteQ3DThemeCall0 call = reinterpret_cast<CuteQ3DThemeCall0>(taken[0]);
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
      CuteQ3DThemeCall1 call = reinterpret_cast<CuteQ3DThemeCall1>(taken[1]);
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
      CuteQ3DThemeCall2 call = reinterpret_cast<CuteQ3DThemeCall2>(taken[2]);
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
      CuteQ3DThemeCall3 call = reinterpret_cast<CuteQ3DThemeCall3>(taken[3]);
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
      CuteQ3DThemeCall4 call = reinterpret_cast<CuteQ3DThemeCall4>(taken[4]);
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
      CuteQ3DThemeCall5 call = reinterpret_cast<CuteQ3DThemeCall5>(taken[5]);
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
      CuteQ3DThemeCall6 call = reinterpret_cast<CuteQ3DThemeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DTheme::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Q3DTheme10metaObjectEv(const Q3DTheme *self) {
  return self->metaObject();
}

//  void *Q3DTheme::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Q3DTheme11qt_metacastEPKc(Q3DTheme *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DTheme::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Q3DTheme11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DTheme *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DTheme::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Q3DTheme2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(Q3DTheme::tr(s, c, n));
}

//  Q3DTheme::Q3DTheme(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZN8Q3DThemeC1EP7QObject(QObject *parent) {
  return new CuteQ3DTheme(parent);
}

//  Q3DTheme::Q3DTheme(Theme themeType, QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZN8Q3DThemeC1ENS_5ThemeEP7QObject(
    Q3DTheme::Theme themeType,
    QObject *parent) {
  return new CuteQ3DTheme(themeType, parent);
}

//  Q3DTheme::~Q3DTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DThemeD1Ev(Q3DTheme *self) {
  delete self;
}

//  void Q3DTheme::setType(Theme themeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme7setTypeENS_5ThemeE(
    Q3DTheme *self,
    Q3DTheme::Theme themeType) {
  self->setType(themeType);
}

//  Theme Q3DTheme::type() const
extern "C" Q_DECL_EXPORT
Q3DTheme::Theme ritual_ZNK8Q3DTheme4typeEv(const Q3DTheme *self) {
  return self->type();
}

//  void Q3DTheme::setBaseColors(const QList<QColor> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme13setBaseColorsERK5QListI6QColorE(
    Q3DTheme *self,
    const QList<QColor> *colors) {
  self->setBaseColors(*colors);
}

//  QList<QColor> Q3DTheme::baseColors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK8Q3DTheme10baseColorsEv(const Q3DTheme *self) {
  return new QList<QColor>(self->baseColors());
}

//  void Q3DTheme::setBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme18setBackgroundColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  QColor Q3DTheme::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme15backgroundColorEv(const Q3DTheme *self) {
  return new QColor(self->backgroundColor());
}

//  void Q3DTheme::setWindowColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme14setWindowColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setWindowColor(*color);
}

//  QColor Q3DTheme::windowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme11windowColorEv(const Q3DTheme *self) {
  return new QColor(self->windowColor());
}

//  void Q3DTheme::setLabelTextColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme17setLabelTextColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setLabelTextColor(*color);
}

//  QColor Q3DTheme::labelTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme14labelTextColorEv(const Q3DTheme *self) {
  return new QColor(self->labelTextColor());
}

//  void Q3DTheme::setLabelBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme23setLabelBackgroundColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setLabelBackgroundColor(*color);
}

//  QColor Q3DTheme::labelBackgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme20labelBackgroundColorEv(const Q3DTheme *self) {
  return new QColor(self->labelBackgroundColor());
}

//  void Q3DTheme::setGridLineColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme16setGridLineColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setGridLineColor(*color);
}

//  QColor Q3DTheme::gridLineColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme13gridLineColorEv(const Q3DTheme *self) {
  return new QColor(self->gridLineColor());
}

//  void Q3DTheme::setSingleHighlightColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme23setSingleHighlightColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setSingleHighlightColor(*color);
}

//  QColor Q3DTheme::singleHighlightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme20singleHighlightColorEv(const Q3DTheme *self) {
  return new QColor(self->singleHighlightColor());
}

//  void Q3DTheme::setMultiHighlightColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme22setMultiHighlightColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setMultiHighlightColor(*color);
}

//  QColor Q3DTheme::multiHighlightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme19multiHighlightColorEv(const Q3DTheme *self) {
  return new QColor(self->multiHighlightColor());
}

//  void Q3DTheme::setLightColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme13setLightColorERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->setLightColor(*color);
}

//  QColor Q3DTheme::lightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8Q3DTheme10lightColorEv(const Q3DTheme *self) {
  return new QColor(self->lightColor());
}

//  void Q3DTheme::setBaseGradients(const QList<QLinearGradient> &gradients)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme16setBaseGradientsERK5QListI15QLinearGradientE(
    Q3DTheme *self,
    const QList<QLinearGradient> *gradients) {
  self->setBaseGradients(*gradients);
}

//  QList<QLinearGradient> Q3DTheme::baseGradients() const
extern "C" Q_DECL_EXPORT
QList<QLinearGradient> *ritual_ZNK8Q3DTheme13baseGradientsEv(
    const Q3DTheme *self) {
  return new QList<QLinearGradient>(self->baseGradients());
}

//  void Q3DTheme::setSingleHighlightGradient(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme26setSingleHighlightGradientERK15QLinearGradient(
    Q3DTheme *self,
    const QLinearGradient *gradient) {
  self->setSingleHighlightGradient(*gradient);
}

//  QLinearGradient Q3DTheme::singleHighlightGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK8Q3DTheme23singleHighlightGradientEv(
    const Q3DTheme *self) {
  return new QLinearGradient(self->singleHighlightGradient());
}

//  void Q3DTheme::setMultiHighlightGradient(const QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme25setMultiHighlightGradientERK15QLinearGradient(
    Q3DTheme *self,
    const QLinearGradient *gradient) {
  self->setMultiHighlightGradient(*gradient);
}

//  QLinearGradient Q3DTheme::multiHighlightGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK8Q3DTheme22multiHighlightGradientEv(
    const Q3DTheme *self) {
  return new QLinearGradient(self->multiHighlightGradient());
}

//  void Q3DTheme::setLightStrength(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme16setLightStrengthEf(Q3DTheme *self, float strength) {
  self->setLightStrength(strength);
}

//  float Q3DTheme::lightStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Q3DTheme13lightStrengthEv(const Q3DTheme *self) {
  return self->lightStrength();
}

//  void Q3DTheme::setAmbientLightStrength(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme23setAmbientLightStrengthEf(
    Q3DTheme *self,
    float strength) {
  self->setAmbientLightStrength(strength);
}

//  float Q3DTheme::ambientLightStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Q3DTheme20ambientLightStrengthEv(const Q3DTheme *self) {
  return self->ambientLightStrength();
}

//  void Q3DTheme::setHighlightLightStrength(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme25setHighlightLightStrengthEf(
    Q3DTheme *self,
    float strength) {
  self->setHighlightLightStrength(strength);
}

//  float Q3DTheme::highlightLightStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Q3DTheme22highlightLightStrengthEv(const Q3DTheme *self) {
  return self->highlightLightStrength();
}

//  void Q3DTheme::setLabelBorderEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme21setLabelBorderEnabledEb(
    Q3DTheme *self,
    bool enabled) {
  self->setLabelBorderEnabled(enabled);
}

//  bool Q3DTheme::isLabelBorderEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Q3DTheme20isLabelBorderEnabledEv(const Q3DTheme *self) {
  return self->isLabelBorderEnabled();
}

//  void Q3DTheme::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme7setFontERK5QFont(Q3DTheme *self, const QFont *font) {
  self->setFont(*font);
}

//  QFont Q3DTheme::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK8Q3DTheme4fontEv(const Q3DTheme *self) {
  return new QFont(self->font());
}

//  void Q3DTheme::setBackgroundEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme20setBackgroundEnabledEb(
    Q3DTheme *self,
    bool enabled) {
  self->setBackgroundEnabled(enabled);
}

//  bool Q3DTheme::isBackgroundEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Q3DTheme19isBackgroundEnabledEv(const Q3DTheme *self) {
  return self->isBackgroundEnabled();
}

//  void Q3DTheme::setGridEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme14setGridEnabledEb(Q3DTheme *self, bool enabled) {
  self->setGridEnabled(enabled);
}

//  bool Q3DTheme::isGridEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Q3DTheme13isGridEnabledEv(const Q3DTheme *self) {
  return self->isGridEnabled();
}

//  void Q3DTheme::setLabelBackgroundEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme25setLabelBackgroundEnabledEb(
    Q3DTheme *self,
    bool enabled) {
  self->setLabelBackgroundEnabled(enabled);
}

//  bool Q3DTheme::isLabelBackgroundEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Q3DTheme24isLabelBackgroundEnabledEv(const Q3DTheme *self) {
  return self->isLabelBackgroundEnabled();
}

//  void Q3DTheme::setColorStyle(ColorStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme13setColorStyleENS_10ColorStyleE(
    Q3DTheme *self,
    Q3DTheme::ColorStyle style) {
  self->setColorStyle(style);
}

//  ColorStyle Q3DTheme::colorStyle() const
extern "C" Q_DECL_EXPORT
Q3DTheme::ColorStyle ritual_ZNK8Q3DTheme10colorStyleEv(
    const Q3DTheme *self) {
  return self->colorStyle();
}

//  void Q3DTheme::typeChanged(Q3DTheme::Theme themeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme11typeChangedENS_5ThemeE(
    Q3DTheme *self,
    Q3DTheme::Theme themeType) {
  self->typeChanged(themeType);
}

//  void Q3DTheme::baseColorsChanged(const QList<QColor> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme17baseColorsChangedERK5QListI6QColorE(
    Q3DTheme *self,
    const QList<QColor> *colors) {
  self->baseColorsChanged(*colors);
}

//  void Q3DTheme::backgroundColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme22backgroundColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->backgroundColorChanged(*color);
}

//  void Q3DTheme::windowColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme18windowColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->windowColorChanged(*color);
}

//  void Q3DTheme::labelTextColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme21labelTextColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->labelTextColorChanged(*color);
}

//  void Q3DTheme::labelBackgroundColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme27labelBackgroundColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->labelBackgroundColorChanged(*color);
}

//  void Q3DTheme::gridLineColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme20gridLineColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->gridLineColorChanged(*color);
}

//  void Q3DTheme::singleHighlightColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme27singleHighlightColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->singleHighlightColorChanged(*color);
}

//  void Q3DTheme::multiHighlightColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme26multiHighlightColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->multiHighlightColorChanged(*color);
}

//  void Q3DTheme::lightColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme17lightColorChangedERK6QColor(
    Q3DTheme *self,
    const QColor *color) {
  self->lightColorChanged(*color);
}

//  void Q3DTheme::baseGradientsChanged(const QList<QLinearGradient>
//      &gradients)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme20baseGradientsChangedERK5QListI15QLinearGradientE(
    Q3DTheme *self,
    const QList<QLinearGradient> *gradients) {
  self->baseGradientsChanged(*gradients);
}

//  void Q3DTheme::singleHighlightGradientChanged(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme30singleHighlightGradientChangedERK15QLinearGradient(
    Q3DTheme *self,
    const QLinearGradient *gradient) {
  self->singleHighlightGradientChanged(*gradient);
}

//  void Q3DTheme::multiHighlightGradientChanged(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme29multiHighlightGradientChangedERK15QLinearGradient(
    Q3DTheme *self,
    const QLinearGradient *gradient) {
  self->multiHighlightGradientChanged(*gradient);
}

//  void Q3DTheme::lightStrengthChanged(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme20lightStrengthChangedEf(
    Q3DTheme *self,
    float strength) {
  self->lightStrengthChanged(strength);
}

//  void Q3DTheme::ambientLightStrengthChanged(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme27ambientLightStrengthChangedEf(
    Q3DTheme *self,
    float strength) {
  self->ambientLightStrengthChanged(strength);
}

//  void Q3DTheme::highlightLightStrengthChanged(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme29highlightLightStrengthChangedEf(
    Q3DTheme *self,
    float strength) {
  self->highlightLightStrengthChanged(strength);
}

//  void Q3DTheme::labelBorderEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme25labelBorderEnabledChangedEb(
    Q3DTheme *self,
    bool enabled) {
  self->labelBorderEnabledChanged(enabled);
}

//  void Q3DTheme::fontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme11fontChangedERK5QFont(
    Q3DTheme *self,
    const QFont *font) {
  self->fontChanged(*font);
}

//  void Q3DTheme::backgroundEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme24backgroundEnabledChangedEb(
    Q3DTheme *self,
    bool enabled) {
  self->backgroundEnabledChanged(enabled);
}

//  void Q3DTheme::gridEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme18gridEnabledChangedEb(Q3DTheme *self, bool enabled) {
  self->gridEnabledChanged(enabled);
}

//  void Q3DTheme::labelBackgroundEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme29labelBackgroundEnabledChangedEb(
    Q3DTheme *self,
    bool enabled) {
  self->labelBackgroundEnabledChanged(enabled);
}

//  void Q3DTheme::colorStyleChanged(Q3DTheme::ColorStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Q3DTheme17colorStyleChangedENS_10ColorStyleE(
    Q3DTheme *self,
    Q3DTheme::ColorStyle style) {
  self->colorStyleChanged(style);
}

//  Q3DTheme::Q3DTheme(Q3DThemePrivate *d, Theme themeType, QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_ZN8Q3DThemeC1EP15Q3DThemePrivateNS_5ThemeEP7QObject(
    Q3DThemePrivate *d,
    Q3DTheme::Theme themeType,
    QObject *parent) {
  return new CuteQ3DTheme(d, themeType, parent);
}

//  a Python function taken by a CuteQ3DTheme, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DTheme(Q3DTheme *self, const char *key, void *call) {
  return static_cast<CuteQ3DTheme *>(self)->take(key, call);
}

//  QList<Q3DTheme *>::QList()
extern "C" Q_DECL_EXPORT
QList<Q3DTheme *> *ritual_list_make_Q3DTheme_ptr() {
  return new QList<Q3DTheme *>();
}

//  void QList<Q3DTheme *>::append(const Q3DTheme * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_Q3DTheme_ptr(
    QList<Q3DTheme *> *self,
    Q3DTheme *element) {
  self->append(element);
}

//  qsizetype QList<Q3DTheme *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_Q3DTheme_ptr(const QList<Q3DTheme *> *self) {
  return self->size();
}

//  const Q3DTheme * &QList<Q3DTheme *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
Q3DTheme *ritual_list_at_Q3DTheme_ptr(
    const QList<Q3DTheme *> *self,
    long long index) {
  return self->at(index);
}

//  QList<Q3DTheme *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_Q3DTheme_ptr(QList<Q3DTheme *> *self) {
  delete self;
}
