//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextcursor.h>

//  const QMetaObject *QGraphicsTextItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGraphicsTextItem10metaObjectEv(
    const QGraphicsTextItem *self) {
  return self->metaObject();
}

//  QString QGraphicsTextItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGraphicsTextItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsTextItem::tr(s, c, n));
}

//  QGraphicsTextItem::QGraphicsTextItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsTextItem *ritual_ZN17QGraphicsTextItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsTextItem(parent);
}

//  QGraphicsTextItem::QGraphicsTextItem(const QString &text, QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
QGraphicsTextItem *ritual_ZN17QGraphicsTextItemC1ERK7QStringP13QGraphicsItem(
    const QString *text,
    QGraphicsItem *parent) {
  return new QGraphicsTextItem(*text, parent);
}

//  QGraphicsTextItem::~QGraphicsTextItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItemD1Ev(QGraphicsTextItem *self) {
  delete self;
}

//  QString QGraphicsTextItem::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGraphicsTextItem6toHtmlEv(
    const QGraphicsTextItem *self) {
  return new QString(self->toHtml());
}

//  void QGraphicsTextItem::setHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem7setHtmlERK7QString(
    QGraphicsTextItem *self,
    const QString *html) {
  self->setHtml(*html);
}

//  QString QGraphicsTextItem::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGraphicsTextItem11toPlainTextEv(
    const QGraphicsTextItem *self) {
  return new QString(self->toPlainText());
}

//  void QGraphicsTextItem::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem12setPlainTextERK7QString(
    QGraphicsTextItem *self,
    const QString *text) {
  self->setPlainText(*text);
}

//  QFont QGraphicsTextItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QGraphicsTextItem4fontEv(const QGraphicsTextItem *self) {
  return new QFont(self->font());
}

//  void QGraphicsTextItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem7setFontERK5QFont(
    QGraphicsTextItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QGraphicsTextItem::setDefaultTextColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem19setDefaultTextColorERK6QColor(
    QGraphicsTextItem *self,
    const QColor *c) {
  self->setDefaultTextColor(*c);
}

//  QColor QGraphicsTextItem::defaultTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QGraphicsTextItem16defaultTextColorEv(
    const QGraphicsTextItem *self) {
  return new QColor(self->defaultTextColor());
}

//  QRectF QGraphicsTextItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsTextItem12boundingRectEv(
    const QGraphicsTextItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsTextItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsTextItem5shapeEv(
    const QGraphicsTextItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsTextItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem8containsERK7QPointF(
    const QGraphicsTextItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsTextItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsTextItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsTextItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsTextItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsTextItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsTextItem10opaqueAreaEv(
    const QGraphicsTextItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsTextItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsTextItem4typeEv(const QGraphicsTextItem *self) {
  return self->type();
}

//  void QGraphicsTextItem::setTextWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem12setTextWidthEd(
    QGraphicsTextItem *self,
    qreal width) {
  self->setTextWidth(width);
}

//  qreal QGraphicsTextItem::textWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGraphicsTextItem9textWidthEv(
    const QGraphicsTextItem *self) {
  return self->textWidth();
}

//  void QGraphicsTextItem::adjustSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem10adjustSizeEv(QGraphicsTextItem *self) {
  self->adjustSize();
}

//  void QGraphicsTextItem::setDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem11setDocumentEP13QTextDocument(
    QGraphicsTextItem *self,
    QTextDocument *document) {
  self->setDocument(document);
}

//  QTextDocument *QGraphicsTextItem::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK17QGraphicsTextItem8documentEv(
    const QGraphicsTextItem *self) {
  return self->document();
}

//  void QGraphicsTextItem::setTextInteractionFlags(Qt::TextInteractionFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QGraphicsTextItem *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QGraphicsTextItem::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsTextItem20textInteractionFlagsEv(
    const QGraphicsTextItem *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QGraphicsTextItem::setTabChangesFocus(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem18setTabChangesFocusEb(
    QGraphicsTextItem *self,
    bool b) {
  self->setTabChangesFocus(b);
}

//  bool QGraphicsTextItem::tabChangesFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem15tabChangesFocusEv(
    const QGraphicsTextItem *self) {
  return self->tabChangesFocus();
}

//  void QGraphicsTextItem::setOpenExternalLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem20setOpenExternalLinksEb(
    QGraphicsTextItem *self,
    bool open) {
  self->setOpenExternalLinks(open);
}

//  bool QGraphicsTextItem::openExternalLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsTextItem17openExternalLinksEv(
    const QGraphicsTextItem *self) {
  return self->openExternalLinks();
}

//  void QGraphicsTextItem::setTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsTextItem13setTextCursorERK11QTextCursor(
    QGraphicsTextItem *self,
    const QTextCursor *cursor) {
  self->setTextCursor(*cursor);
}

//  QTextCursor QGraphicsTextItem::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK17QGraphicsTextItem10textCursorEv(
    const QGraphicsTextItem *self) {
  return new QTextCursor(self->textCursor());
}
