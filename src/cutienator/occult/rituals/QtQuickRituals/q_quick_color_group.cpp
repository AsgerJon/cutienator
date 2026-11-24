//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcolorgroup_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcolorgroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuickColorGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickColorGroup : QQuickColorGroup {
  using QQuickColorGroup::currentColorGroup;
};

//  const QMetaObject *QQuickColorGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickColorGroup10metaObjectEv(
    const QQuickColorGroup *self) {
  return self->metaObject();
}

//  QString QQuickColorGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickColorGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickColorGroup::tr(s, c, n));
}

//  QQuickColorGroup::QQuickColorGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickColorGroup *ritual_ZN16QQuickColorGroupC1EP7QObject(QObject *parent) {
  return new QQuickColorGroup(parent);
}

//  QColor QQuickColorGroup::alternateBase() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup13alternateBaseEv(
    const QQuickColorGroup *self) {
  return new QColor(self->alternateBase());
}

//  void QQuickColorGroup::setAlternateBase(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup16setAlternateBaseERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setAlternateBase(*color);
}

//  void QQuickColorGroup::resetAlternateBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup18resetAlternateBaseEv(
    QQuickColorGroup *self) {
  self->resetAlternateBase();
}

//  QColor QQuickColorGroup::base() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup4baseEv(const QQuickColorGroup *self) {
  return new QColor(self->base());
}

//  void QQuickColorGroup::setBase(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup7setBaseERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setBase(*color);
}

//  void QQuickColorGroup::resetBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9resetBaseEv(QQuickColorGroup *self) {
  self->resetBase();
}

//  QColor QQuickColorGroup::brightText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup10brightTextEv(
    const QQuickColorGroup *self) {
  return new QColor(self->brightText());
}

//  void QQuickColorGroup::setBrightText(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup13setBrightTextERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setBrightText(*color);
}

//  void QQuickColorGroup::resetBrightText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup15resetBrightTextEv(QQuickColorGroup *self) {
  self->resetBrightText();
}

//  QColor QQuickColorGroup::button() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup6buttonEv(const QQuickColorGroup *self) {
  return new QColor(self->button());
}

//  void QQuickColorGroup::setButton(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9setButtonERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setButton(*color);
}

//  void QQuickColorGroup::resetButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup11resetButtonEv(QQuickColorGroup *self) {
  self->resetButton();
}

//  QColor QQuickColorGroup::buttonText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup10buttonTextEv(
    const QQuickColorGroup *self) {
  return new QColor(self->buttonText());
}

//  void QQuickColorGroup::setButtonText(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup13setButtonTextERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setButtonText(*color);
}

//  void QQuickColorGroup::resetButtonText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup15resetButtonTextEv(QQuickColorGroup *self) {
  self->resetButtonText();
}

//  QColor QQuickColorGroup::dark() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup4darkEv(const QQuickColorGroup *self) {
  return new QColor(self->dark());
}

//  void QQuickColorGroup::setDark(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup7setDarkERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setDark(*color);
}

//  void QQuickColorGroup::resetDark()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9resetDarkEv(QQuickColorGroup *self) {
  self->resetDark();
}

//  QColor QQuickColorGroup::highlight() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup9highlightEv(
    const QQuickColorGroup *self) {
  return new QColor(self->highlight());
}

//  void QQuickColorGroup::setHighlight(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup12setHighlightERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setHighlight(*color);
}

//  void QQuickColorGroup::resetHighlight()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup14resetHighlightEv(QQuickColorGroup *self) {
  self->resetHighlight();
}

//  QColor QQuickColorGroup::highlightedText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup15highlightedTextEv(
    const QQuickColorGroup *self) {
  return new QColor(self->highlightedText());
}

//  void QQuickColorGroup::setHighlightedText(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup18setHighlightedTextERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setHighlightedText(*color);
}

//  void QQuickColorGroup::resetHighlightedText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup20resetHighlightedTextEv(
    QQuickColorGroup *self) {
  self->resetHighlightedText();
}

//  QColor QQuickColorGroup::light() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup5lightEv(const QQuickColorGroup *self) {
  return new QColor(self->light());
}

//  void QQuickColorGroup::setLight(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup8setLightERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setLight(*color);
}

//  void QQuickColorGroup::resetLight()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup10resetLightEv(QQuickColorGroup *self) {
  self->resetLight();
}

//  QColor QQuickColorGroup::link() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup4linkEv(const QQuickColorGroup *self) {
  return new QColor(self->link());
}

//  void QQuickColorGroup::setLink(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup7setLinkERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setLink(*color);
}

//  void QQuickColorGroup::resetLink()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9resetLinkEv(QQuickColorGroup *self) {
  self->resetLink();
}

//  QColor QQuickColorGroup::linkVisited() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup11linkVisitedEv(
    const QQuickColorGroup *self) {
  return new QColor(self->linkVisited());
}

//  void QQuickColorGroup::setLinkVisited(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup14setLinkVisitedERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setLinkVisited(*color);
}

//  void QQuickColorGroup::resetLinkVisited()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup16resetLinkVisitedEv(
    QQuickColorGroup *self) {
  self->resetLinkVisited();
}

//  QColor QQuickColorGroup::mid() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup3midEv(const QQuickColorGroup *self) {
  return new QColor(self->mid());
}

//  void QQuickColorGroup::setMid(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup6setMidERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setMid(*color);
}

//  void QQuickColorGroup::resetMid()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup8resetMidEv(QQuickColorGroup *self) {
  self->resetMid();
}

//  QColor QQuickColorGroup::midlight() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup8midlightEv(
    const QQuickColorGroup *self) {
  return new QColor(self->midlight());
}

//  void QQuickColorGroup::setMidlight(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup11setMidlightERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setMidlight(*color);
}

//  void QQuickColorGroup::resetMidlight()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup13resetMidlightEv(QQuickColorGroup *self) {
  self->resetMidlight();
}

//  QColor QQuickColorGroup::shadow() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup6shadowEv(const QQuickColorGroup *self) {
  return new QColor(self->shadow());
}

//  void QQuickColorGroup::setShadow(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9setShadowERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setShadow(*color);
}

//  void QQuickColorGroup::resetShadow()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup11resetShadowEv(QQuickColorGroup *self) {
  self->resetShadow();
}

//  QColor QQuickColorGroup::text() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup4textEv(const QQuickColorGroup *self) {
  return new QColor(self->text());
}

//  void QQuickColorGroup::setText(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup7setTextERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setText(*color);
}

//  void QQuickColorGroup::resetText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9resetTextEv(QQuickColorGroup *self) {
  self->resetText();
}

//  QColor QQuickColorGroup::toolTipBase() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup11toolTipBaseEv(
    const QQuickColorGroup *self) {
  return new QColor(self->toolTipBase());
}

//  void QQuickColorGroup::setToolTipBase(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup14setToolTipBaseERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setToolTipBase(*color);
}

//  void QQuickColorGroup::resetToolTipBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup16resetToolTipBaseEv(
    QQuickColorGroup *self) {
  self->resetToolTipBase();
}

//  QColor QQuickColorGroup::toolTipText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup11toolTipTextEv(
    const QQuickColorGroup *self) {
  return new QColor(self->toolTipText());
}

//  void QQuickColorGroup::setToolTipText(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup14setToolTipTextERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setToolTipText(*color);
}

//  void QQuickColorGroup::resetToolTipText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup16resetToolTipTextEv(
    QQuickColorGroup *self) {
  self->resetToolTipText();
}

//  QColor QQuickColorGroup::window() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup6windowEv(const QQuickColorGroup *self) {
  return new QColor(self->window());
}

//  void QQuickColorGroup::setWindow(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9setWindowERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setWindow(*color);
}

//  void QQuickColorGroup::resetWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup11resetWindowEv(QQuickColorGroup *self) {
  self->resetWindow();
}

//  QColor QQuickColorGroup::windowText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup10windowTextEv(
    const QQuickColorGroup *self) {
  return new QColor(self->windowText());
}

//  void QQuickColorGroup::setWindowText(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup13setWindowTextERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setWindowText(*color);
}

//  void QQuickColorGroup::resetWindowText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup15resetWindowTextEv(QQuickColorGroup *self) {
  self->resetWindowText();
}

//  QColor QQuickColorGroup::placeholderText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup15placeholderTextEv(
    const QQuickColorGroup *self) {
  return new QColor(self->placeholderText());
}

//  void QQuickColorGroup::setPlaceholderText(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup18setPlaceholderTextERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setPlaceholderText(*color);
}

//  void QQuickColorGroup::resetPlaceholderText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup20resetPlaceholderTextEv(
    QQuickColorGroup *self) {
  self->resetPlaceholderText();
}

//  QColor QQuickColorGroup::accent() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup6accentEv(const QQuickColorGroup *self) {
  return new QColor(self->accent());
}

//  void QQuickColorGroup::setAccent(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup9setAccentERK6QColor(
    QQuickColorGroup *self,
    const QColor *color) {
  self->setAccent(*color);
}

//  void QQuickColorGroup::resetAccent()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup11resetAccentEv(QQuickColorGroup *self) {
  self->resetAccent();
}

//  QPalette::ColorGroup QQuickColorGroup::groupTag() const
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_ZNK16QQuickColorGroup8groupTagEv(
    const QQuickColorGroup *self) {
  return self->groupTag();
}

//  void QQuickColorGroup::setGroupTag(QPalette::ColorGroup tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickColorGroup11setGroupTagEN8QPalette10ColorGroupE(
    QQuickColorGroup *self,
    QPalette::ColorGroup tag) {
  self->setGroupTag(tag);
}

//  QPalette::ColorGroup QQuickColorGroup::defaultGroupTag()
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_ZN16QQuickColorGroup15defaultGroupTagEv() {
  return QQuickColorGroup::defaultGroupTag();
}

//  QPalette::ColorGroup QQuickColorGroup::currentColorGroup() const
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_ZNK16QQuickColorGroup17currentColorGroupEv(
    const QQuickColorGroup *self) {
  return self->currentColorGroup();
}

//  QColor QQuickColorGroup::color(QPalette::ColorRole role) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QQuickColorGroup5colorEN8QPalette9ColorRoleE(
    const QQuickColorGroup *self,
    QPalette::ColorRole role) {
  return new QColor(self->color(role));
}

//  QPalette::ColorGroup QQuickColorGroup::currentColorGroup() const
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_own_ZNK16QQuickColorGroup17currentColorGroupEv(
    const QQuickColorGroup *self) {
  return static_cast<const OwnQQuickColorGroup *>(self)->OwnQQuickColorGroup::currentColorGroup();
}
