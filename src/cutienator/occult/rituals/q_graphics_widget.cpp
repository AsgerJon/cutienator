//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicswidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicswidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtGui/qkeysequence.h>
#include <QtGui/qpainterpath.h>

//  const QMetaObject *QGraphicsWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsWidget10metaObjectEv(
    const QGraphicsWidget *self) {
  return self->metaObject();
}

//  QString QGraphicsWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsWidget::tr(s, c, n));
}

//  QGraphicsWidget::QGraphicsWidget(QGraphicsItem *parent, Qt::WindowFlags
//      wFlags)
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZN15QGraphicsWidgetC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsItem *parent,
    int wFlags) {
  return new QGraphicsWidget(
      parent,
      QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QGraphicsWidget::~QGraphicsWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidgetD1Ev(QGraphicsWidget *self) {
  delete self;
}

//  QGraphicsLayout *QGraphicsWidget::layout() const
extern "C" Q_DECL_EXPORT
QGraphicsLayout *ritual_ZNK15QGraphicsWidget6layoutEv(
    const QGraphicsWidget *self) {
  return self->layout();
}

//  void QGraphicsWidget::setLayout(QGraphicsLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget9setLayoutEP15QGraphicsLayout(
    QGraphicsWidget *self,
    QGraphicsLayout *layout) {
  self->setLayout(layout);
}

//  void QGraphicsWidget::adjustSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget10adjustSizeEv(QGraphicsWidget *self) {
  self->adjustSize();
}

//  Qt::LayoutDirection QGraphicsWidget::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK15QGraphicsWidget15layoutDirectionEv(
    const QGraphicsWidget *self) {
  return self->layoutDirection();
}

//  void QGraphicsWidget::setLayoutDirection(Qt::LayoutDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QGraphicsWidget *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection(direction);
}

//  void QGraphicsWidget::unsetLayoutDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget20unsetLayoutDirectionEv(
    QGraphicsWidget *self) {
  self->unsetLayoutDirection();
}

//  QStyle *QGraphicsWidget::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK15QGraphicsWidget5styleEv(const QGraphicsWidget *self) {
  return self->style();
}

//  void QGraphicsWidget::setStyle(QStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget8setStyleEP6QStyle(
    QGraphicsWidget *self,
    QStyle *style) {
  self->setStyle(style);
}

//  QFont QGraphicsWidget::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QGraphicsWidget4fontEv(const QGraphicsWidget *self) {
  return new QFont(self->font());
}

//  void QGraphicsWidget::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget7setFontERK5QFont(
    QGraphicsWidget *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QPalette QGraphicsWidget::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK15QGraphicsWidget7paletteEv(
    const QGraphicsWidget *self) {
  return new QPalette(self->palette());
}

//  void QGraphicsWidget::setPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget10setPaletteERK8QPalette(
    QGraphicsWidget *self,
    const QPalette *palette) {
  self->setPalette(*palette);
}

//  bool QGraphicsWidget::autoFillBackground() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsWidget18autoFillBackgroundEv(
    const QGraphicsWidget *self) {
  return self->autoFillBackground();
}

//  void QGraphicsWidget::setAutoFillBackground(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setAutoFillBackgroundEb(
    QGraphicsWidget *self,
    bool enabled) {
  self->setAutoFillBackground(enabled);
}

//  void QGraphicsWidget::resize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget6resizeERK6QSizeF(
    QGraphicsWidget *self,
    const QSizeF *size) {
  self->resize(*size);
}

//  void QGraphicsWidget::resize(qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget6resizeEdd(
    QGraphicsWidget *self,
    qreal w,
    qreal h) {
  self->resize(w, h);
}

//  QSizeF QGraphicsWidget::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QGraphicsWidget4sizeEv(const QGraphicsWidget *self) {
  return new QSizeF(self->size());
}

//  void QGraphicsWidget::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11setGeometryERK6QRectF(
    QGraphicsWidget *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  void QGraphicsWidget::setGeometry(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11setGeometryEdddd(
    QGraphicsWidget *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setGeometry(x, y, w, h);
}

//  QRectF QGraphicsWidget::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget4rectEv(const QGraphicsWidget *self) {
  return new QRectF(self->rect());
}

//  void QGraphicsWidget::setContentsMargins(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setContentsMarginsEdddd(
    QGraphicsWidget *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setContentsMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::setContentsMargins(QMarginsF margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setContentsMarginsE9QMarginsF(
    QGraphicsWidget *self,
    const QMarginsF *margins) {
  self->setContentsMargins(*margins);
}

//  void QGraphicsWidget::getContentsMargins(qreal *left, qreal *top, qreal
//      *right, qreal *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QGraphicsWidget18getContentsMarginsEPdS0_S0_S0_(
    const QGraphicsWidget *self,
    qreal *left,
    qreal *top,
    qreal *right,
    qreal *bottom) {
  self->getContentsMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::setWindowFrameMargins(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setWindowFrameMarginsEdddd(
    QGraphicsWidget *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setWindowFrameMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::setWindowFrameMargins(QMarginsF margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setWindowFrameMarginsE9QMarginsF(
    QGraphicsWidget *self,
    const QMarginsF *margins) {
  self->setWindowFrameMargins(*margins);
}

//  void QGraphicsWidget::getWindowFrameMargins(qreal *left, qreal *top,
//      qreal *right, qreal *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QGraphicsWidget21getWindowFrameMarginsEPdS0_S0_S0_(
    const QGraphicsWidget *self,
    qreal *left,
    qreal *top,
    qreal *right,
    qreal *bottom) {
  self->getWindowFrameMargins(left, top, right, bottom);
}

//  void QGraphicsWidget::unsetWindowFrameMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget23unsetWindowFrameMarginsEv(
    QGraphicsWidget *self) {
  self->unsetWindowFrameMargins();
}

//  QRectF QGraphicsWidget::windowFrameGeometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget19windowFrameGeometryEv(
    const QGraphicsWidget *self) {
  return new QRectF(self->windowFrameGeometry());
}

//  QRectF QGraphicsWidget::windowFrameRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget15windowFrameRectEv(
    const QGraphicsWidget *self) {
  return new QRectF(self->windowFrameRect());
}

//  Qt::WindowFlags QGraphicsWidget::windowFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGraphicsWidget11windowFlagsEv(const QGraphicsWidget *self) {
  return static_cast<int>(self->windowFlags().toInt());
}

//  Qt::WindowType QGraphicsWidget::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK15QGraphicsWidget10windowTypeEv(
    const QGraphicsWidget *self) {
  return self->windowType();
}

//  void QGraphicsWidget::setWindowFlags(Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsWidget *self,
    int wFlags) {
  self->setWindowFlags(QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  bool QGraphicsWidget::isActiveWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsWidget14isActiveWindowEv(
    const QGraphicsWidget *self) {
  return self->isActiveWindow();
}

//  void QGraphicsWidget::setWindowTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14setWindowTitleERK7QString(
    QGraphicsWidget *self,
    const QString *title) {
  self->setWindowTitle(*title);
}

//  QString QGraphicsWidget::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QGraphicsWidget11windowTitleEv(
    const QGraphicsWidget *self) {
  return new QString(self->windowTitle());
}

//  Qt::FocusPolicy QGraphicsWidget::focusPolicy() const
extern "C" Q_DECL_EXPORT
Qt::FocusPolicy ritual_ZNK15QGraphicsWidget11focusPolicyEv(
    const QGraphicsWidget *self) {
  return self->focusPolicy();
}

//  void QGraphicsWidget::setFocusPolicy(Qt::FocusPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget14setFocusPolicyEN2Qt11FocusPolicyE(
    QGraphicsWidget *self,
    Qt::FocusPolicy policy) {
  self->setFocusPolicy(policy);
}

//  void QGraphicsWidget::setTabOrder(QGraphicsWidget *first, QGraphicsWidget
//      *second)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget11setTabOrderEPS_S0_(
    QGraphicsWidget *first,
    QGraphicsWidget *second) {
  QGraphicsWidget::setTabOrder(first, second);
}

//  QGraphicsWidget *QGraphicsWidget::focusWidget() const
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZNK15QGraphicsWidget11focusWidgetEv(
    const QGraphicsWidget *self) {
  return self->focusWidget();
}

//  int QGraphicsWidget::grabShortcut(const QKeySequence &sequence,
//      Qt::ShortcutContext context)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGraphicsWidget12grabShortcutERK12QKeySequenceN2Qt15ShortcutContextE(
    QGraphicsWidget *self,
    const QKeySequence *sequence,
    Qt::ShortcutContext context) {
  return self->grabShortcut(*sequence, context);
}

//  void QGraphicsWidget::releaseShortcut(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget15releaseShortcutEi(
    QGraphicsWidget *self,
    int id) {
  self->releaseShortcut(id);
}

//  void QGraphicsWidget::setShortcutEnabled(int id, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget18setShortcutEnabledEib(
    QGraphicsWidget *self,
    int id,
    bool enabled) {
  self->setShortcutEnabled(id, enabled);
}

//  void QGraphicsWidget::setShortcutAutoRepeat(int id, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget21setShortcutAutoRepeatEib(
    QGraphicsWidget *self,
    int id,
    bool enabled) {
  self->setShortcutAutoRepeat(id, enabled);
}

//  void QGraphicsWidget::addAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget9addActionEP7QAction(
    QGraphicsWidget *self,
    QAction *action) {
  self->addAction(action);
}

//  void QGraphicsWidget::insertAction(QAction *before, QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget12insertActionEP7QActionS1_(
    QGraphicsWidget *self,
    QAction *before,
    QAction *action) {
  self->insertAction(before, action);
}

//  void QGraphicsWidget::removeAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget12removeActionEP7QAction(
    QGraphicsWidget *self,
    QAction *action) {
  self->removeAction(action);
}

//  void QGraphicsWidget::setAttribute(Qt::WidgetAttribute attribute, bool
//      on)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget12setAttributeEN2Qt15WidgetAttributeEb(
    QGraphicsWidget *self,
    Qt::WidgetAttribute attribute,
    bool on) {
  self->setAttribute(attribute, on);
}

//  bool QGraphicsWidget::testAttribute(Qt::WidgetAttribute attribute) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsWidget13testAttributeEN2Qt15WidgetAttributeE(
    const QGraphicsWidget *self,
    Qt::WidgetAttribute attribute) {
  return self->testAttribute(attribute);
}

//  int QGraphicsWidget::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGraphicsWidget4typeEv(const QGraphicsWidget *self) {
  return self->type();
}

//  void QGraphicsWidget::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void QGraphicsWidget::paintWindowFrame(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsWidget16paintWindowFrameEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsWidget *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paintWindowFrame(painter, option, widget);
}

//  QRectF QGraphicsWidget::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsWidget12boundingRectEv(
    const QGraphicsWidget *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsWidget::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK15QGraphicsWidget5shapeEv(
    const QGraphicsWidget *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsWidget::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsWidget5closeEv(QGraphicsWidget *self) {
  return self->close();
}
