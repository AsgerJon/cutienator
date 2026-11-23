//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpalette.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpalette.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtCore/qvariant.h>

//  QPalette::QPalette()
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QPaletteC1Ev() {
  return new QPalette();
}

//  QPalette::QPalette(const QColor &button)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QPaletteC1ERK6QColor(const QColor *button) {
  return new QPalette(*button);
}

//  QPalette::QPalette(Qt::GlobalColor button)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QPaletteC1EN2Qt11GlobalColorE(Qt::GlobalColor button) {
  return new QPalette(button);
}

//  QPalette::QPalette(const QColor &button, const QColor &window)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QPaletteC1ERK6QColorS2_(
    const QColor *button,
    const QColor *window) {
  return new QPalette(*button, *window);
}

//  QPalette::QPalette(const QBrush &windowText, const QBrush &button, const
//      QBrush &light, const QBrush &dark, const QBrush &mid, const QBrush
//      &text, const QBrush &bright_text, const QBrush &base, const QBrush
//      &window)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QPaletteC1ERK6QBrushS2_S2_S2_S2_S2_S2_S2_S2_(
    const QBrush *windowText,
    const QBrush *button,
    const QBrush *light,
    const QBrush *dark,
    const QBrush *mid,
    const QBrush *text,
    const QBrush *bright_text,
    const QBrush *base,
    const QBrush *window) {
  return new QPalette(
      *windowText,
      *button,
      *light,
      *dark,
      *mid,
      *text,
      *bright_text,
      *base,
      *window);
}

//  QPalette::QPalette(const QColor &windowText, const QColor &window, const
//      QColor &light, const QColor &dark, const QColor &mid, const QColor
//      &text, const QColor &base)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QPaletteC1ERK6QColorS2_S2_S2_S2_S2_S2_(
    const QColor *windowText,
    const QColor *window,
    const QColor *light,
    const QColor *dark,
    const QColor *mid,
    const QColor *text,
    const QColor *base) {
  return new QPalette(
      *windowText,
      *window,
      *light,
      *dark,
      *mid,
      *text,
      *base);
}

//  QPalette::QPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZN8QPaletteC1ERKS_(const QPalette *palette) {
  return new QPalette(*palette);
}

//  QPalette::~QPalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPaletteD1Ev(QPalette *self) {
  delete self;
}

//  QVariant QPalette::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QPalettecv8QVariantEv(const QPalette *self) {
  return new QVariant(self->operator QVariant());
}

//  ColorGroup QPalette::currentColorGroup() const
extern "C" Q_DECL_EXPORT
QPalette::ColorGroup ritual_ZNK8QPalette17currentColorGroupEv(
    const QPalette *self) {
  return self->currentColorGroup();
}

//  void QPalette::setCurrentColorGroup(ColorGroup cg)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette20setCurrentColorGroupENS_10ColorGroupE(
    QPalette *self,
    QPalette::ColorGroup cg) {
  self->setCurrentColorGroup(cg);
}

//  const QColor &QPalette::color(ColorGroup cg, ColorRole cr) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8QPalette5colorENS_10ColorGroupENS_9ColorRoleE(
    const QPalette *self,
    QPalette::ColorGroup cg,
    QPalette::ColorRole cr) {
  return new QColor(self->color(cg, cr));
}

//  const QBrush &QPalette::brush(ColorGroup cg, ColorRole cr) const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette5brushENS_10ColorGroupENS_9ColorRoleE(
    const QPalette *self,
    QPalette::ColorGroup cg,
    QPalette::ColorRole cr) {
  return new QBrush(self->brush(cg, cr));
}

//  void QPalette::setColor(ColorGroup cg, ColorRole cr, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette8setColorENS_10ColorGroupENS_9ColorRoleERK6QColor(
    QPalette *self,
    QPalette::ColorGroup cg,
    QPalette::ColorRole cr,
    const QColor *color) {
  self->setColor(cg, cr, *color);
}

//  void QPalette::setColor(ColorRole cr, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette8setColorENS_9ColorRoleERK6QColor(
    QPalette *self,
    QPalette::ColorRole cr,
    const QColor *color) {
  self->setColor(cr, *color);
}

//  void QPalette::setBrush(ColorRole cr, const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette8setBrushENS_9ColorRoleERK6QBrush(
    QPalette *self,
    QPalette::ColorRole cr,
    const QBrush *brush) {
  self->setBrush(cr, *brush);
}

//  bool QPalette::isBrushSet(ColorGroup cg, ColorRole cr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPalette10isBrushSetENS_10ColorGroupENS_9ColorRoleE(
    const QPalette *self,
    QPalette::ColorGroup cg,
    QPalette::ColorRole cr) {
  return self->isBrushSet(cg, cr);
}

//  void QPalette::setBrush(ColorGroup cg, ColorRole cr, const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette8setBrushENS_10ColorGroupENS_9ColorRoleERK6QBrush(
    QPalette *self,
    QPalette::ColorGroup cg,
    QPalette::ColorRole cr,
    const QBrush *brush) {
  self->setBrush(cg, cr, *brush);
}

//  void QPalette::setColorGroup(ColorGroup cr, const QBrush &windowText,
//      const QBrush &button, const QBrush &light, const QBrush &dark, const
//      QBrush &mid, const QBrush &text, const QBrush &bright_text, const
//      QBrush &base, const QBrush &window)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette13setColorGroupENS_10ColorGroupERK6QBrushS3_S3_S3_S3_S3_S3_S3_S3_(
    QPalette *self,
    QPalette::ColorGroup cr,
    const QBrush *windowText,
    const QBrush *button,
    const QBrush *light,
    const QBrush *dark,
    const QBrush *mid,
    const QBrush *text,
    const QBrush *bright_text,
    const QBrush *base,
    const QBrush *window) {
  self->setColorGroup(
      cr,
      *windowText,
      *button,
      *light,
      *dark,
      *mid,
      *text,
      *bright_text,
      *base,
      *window);
}

//  bool QPalette::isEqual(ColorGroup cr1, ColorGroup cr2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPalette7isEqualENS_10ColorGroupES0_(
    const QPalette *self,
    QPalette::ColorGroup cr1,
    QPalette::ColorGroup cr2) {
  return self->isEqual(cr1, cr2);
}

//  const QColor &QPalette::color(ColorRole cr) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8QPalette5colorENS_9ColorRoleE(
    const QPalette *self,
    QPalette::ColorRole cr) {
  return new QColor(self->color(cr));
}

//  const QBrush &QPalette::brush(ColorRole cr) const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette5brushENS_9ColorRoleE(
    const QPalette *self,
    QPalette::ColorRole cr) {
  return new QBrush(self->brush(cr));
}

//  const QBrush &QPalette::windowText() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette10windowTextEv(const QPalette *self) {
  return new QBrush(self->windowText());
}

//  const QBrush &QPalette::button() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette6buttonEv(const QPalette *self) {
  return new QBrush(self->button());
}

//  const QBrush &QPalette::light() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette5lightEv(const QPalette *self) {
  return new QBrush(self->light());
}

//  const QBrush &QPalette::dark() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette4darkEv(const QPalette *self) {
  return new QBrush(self->dark());
}

//  const QBrush &QPalette::mid() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette3midEv(const QPalette *self) {
  return new QBrush(self->mid());
}

//  const QBrush &QPalette::text() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette4textEv(const QPalette *self) {
  return new QBrush(self->text());
}

//  const QBrush &QPalette::base() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette4baseEv(const QPalette *self) {
  return new QBrush(self->base());
}

//  const QBrush &QPalette::alternateBase() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette13alternateBaseEv(const QPalette *self) {
  return new QBrush(self->alternateBase());
}

//  const QBrush &QPalette::toolTipBase() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette11toolTipBaseEv(const QPalette *self) {
  return new QBrush(self->toolTipBase());
}

//  const QBrush &QPalette::toolTipText() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette11toolTipTextEv(const QPalette *self) {
  return new QBrush(self->toolTipText());
}

//  const QBrush &QPalette::window() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette6windowEv(const QPalette *self) {
  return new QBrush(self->window());
}

//  const QBrush &QPalette::midlight() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette8midlightEv(const QPalette *self) {
  return new QBrush(self->midlight());
}

//  const QBrush &QPalette::brightText() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette10brightTextEv(const QPalette *self) {
  return new QBrush(self->brightText());
}

//  const QBrush &QPalette::buttonText() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette10buttonTextEv(const QPalette *self) {
  return new QBrush(self->buttonText());
}

//  const QBrush &QPalette::shadow() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette6shadowEv(const QPalette *self) {
  return new QBrush(self->shadow());
}

//  const QBrush &QPalette::highlight() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette9highlightEv(const QPalette *self) {
  return new QBrush(self->highlight());
}

//  const QBrush &QPalette::highlightedText() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette15highlightedTextEv(const QPalette *self) {
  return new QBrush(self->highlightedText());
}

//  const QBrush &QPalette::link() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette4linkEv(const QPalette *self) {
  return new QBrush(self->link());
}

//  const QBrush &QPalette::linkVisited() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette11linkVisitedEv(const QPalette *self) {
  return new QBrush(self->linkVisited());
}

//  const QBrush &QPalette::placeholderText() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette15placeholderTextEv(const QPalette *self) {
  return new QBrush(self->placeholderText());
}

//  const QBrush &QPalette::accent() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QPalette6accentEv(const QPalette *self) {
  return new QBrush(self->accent());
}

//  bool QPalette::operator==(const QPalette &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPaletteeqERKS_(const QPalette *self, const QPalette *p) {
  return self->operator==(*p);
}

//  bool QPalette::operator!=(const QPalette &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPaletteneERKS_(const QPalette *self, const QPalette *p) {
  return self->operator!=(*p);
}

//  bool QPalette::isCopyOf(const QPalette &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPalette8isCopyOfERKS_(
    const QPalette *self,
    const QPalette *p) {
  return self->isCopyOf(*p);
}

//  qint64 QPalette::cacheKey() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK8QPalette8cacheKeyEv(const QPalette *self) {
  return self->cacheKey();
}

//  QPalette QPalette::resolve(const QPalette &other) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK8QPalette7resolveERKS_(
    const QPalette *self,
    const QPalette *other) {
  return new QPalette(self->resolve(*other));
}

//  ResolveMask QPalette::resolveMask() const
extern "C" Q_DECL_EXPORT
QPalette::ResolveMask ritual_ZNK8QPalette11resolveMaskEv(
    const QPalette *self) {
  return self->resolveMask();
}

//  void QPalette::setResolveMask(ResolveMask mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette14setResolveMaskEy(
    QPalette *self,
    QPalette::ResolveMask mask) {
  self->setResolveMask(mask);
}

//  void QPalette::setColorGroup(ColorGroup cr, const QBrush &windowText,
//      const QBrush &button, const QBrush &light, const QBrush &dark, const
//      QBrush &mid, const QBrush &text, const QBrush &bright_text, const
//      QBrush &base, const QBrush &alternate_base, const QBrush &window,
//      const QBrush &midlight, const QBrush &button_text, const QBrush
//      &shadow, const QBrush &highlight, const QBrush &highlighted_text,
//      const QBrush &link, const QBrush &link_visited)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette13setColorGroupENS_10ColorGroupERK6QBrushS3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_(
    QPalette *self,
    QPalette::ColorGroup cr,
    const QBrush *windowText,
    const QBrush *button,
    const QBrush *light,
    const QBrush *dark,
    const QBrush *mid,
    const QBrush *text,
    const QBrush *bright_text,
    const QBrush *base,
    const QBrush *alternate_base,
    const QBrush *window,
    const QBrush *midlight,
    const QBrush *button_text,
    const QBrush *shadow,
    const QBrush *highlight,
    const QBrush *highlighted_text,
    const QBrush *link,
    const QBrush *link_visited) {
  self->setColorGroup(
      cr,
      *windowText,
      *button,
      *light,
      *dark,
      *mid,
      *text,
      *bright_text,
      *base,
      *alternate_base,
      *window,
      *midlight,
      *button_text,
      *shadow,
      *highlight,
      *highlighted_text,
      *link,
      *link_visited);
}

//  void QPalette::setColorGroup(ColorGroup cr, const QBrush &windowText,
//      const QBrush &button, const QBrush &light, const QBrush &dark, const
//      QBrush &mid, const QBrush &text, const QBrush &bright_text, const
//      QBrush &base, const QBrush &alternate_base, const QBrush &window,
//      const QBrush &midlight, const QBrush &button_text, const QBrush
//      &shadow, const QBrush &highlight, const QBrush &highlighted_text,
//      const QBrush &link, const QBrush &link_visited, const QBrush
//      &toolTipBase, const QBrush &toolTipText)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette13setColorGroupENS_10ColorGroupERK6QBrushS3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_S3_(
    QPalette *self,
    QPalette::ColorGroup cr,
    const QBrush *windowText,
    const QBrush *button,
    const QBrush *light,
    const QBrush *dark,
    const QBrush *mid,
    const QBrush *text,
    const QBrush *bright_text,
    const QBrush *base,
    const QBrush *alternate_base,
    const QBrush *window,
    const QBrush *midlight,
    const QBrush *button_text,
    const QBrush *shadow,
    const QBrush *highlight,
    const QBrush *highlighted_text,
    const QBrush *link,
    const QBrush *link_visited,
    const QBrush *toolTipBase,
    const QBrush *toolTipText) {
  self->setColorGroup(
      cr,
      *windowText,
      *button,
      *light,
      *dark,
      *mid,
      *text,
      *bright_text,
      *base,
      *alternate_base,
      *window,
      *midlight,
      *button_text,
      *shadow,
      *highlight,
      *highlighted_text,
      *link,
      *link_visited,
      *toolTipBase,
      *toolTipText);
}

//  void QPalette::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette4initEv(QPalette *self) {
  self->init();
}

//  void QPalette::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPalette6detachEv(QPalette *self) {
  self->detach();
}
