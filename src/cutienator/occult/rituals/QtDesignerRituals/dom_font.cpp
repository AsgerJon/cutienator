//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomFont::DomFont()
extern "C" Q_DECL_EXPORT
DomFont *ritual_ZN7DomFontC1Ev() {
  return new DomFont();
}

//  DomFont::~DomFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFontD1Ev(DomFont *self) {
  delete self;
}

//  void DomFont::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont4readER16QXmlStreamReader(
    DomFont *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomFont::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7DomFont5writeER16QXmlStreamWriterRK7QString(
    const DomFont *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QString DomFont::elementFamily() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7DomFont13elementFamilyEv(const DomFont *self) {
  return new QString(self->elementFamily());
}

//  void DomFont::setElementFamily(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont16setElementFamilyERK7QString(
    DomFont *self,
    const QString *a) {
  self->setElementFamily(*a);
}

//  bool DomFont::hasElementFamily() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont16hasElementFamilyEv(const DomFont *self) {
  return self->hasElementFamily();
}

//  void DomFont::clearElementFamily()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont18clearElementFamilyEv(DomFont *self) {
  self->clearElementFamily();
}

//  int DomFont::elementPointSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7DomFont16elementPointSizeEv(const DomFont *self) {
  return self->elementPointSize();
}

//  void DomFont::setElementPointSize(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont19setElementPointSizeEi(DomFont *self, int a) {
  self->setElementPointSize(a);
}

//  bool DomFont::hasElementPointSize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont19hasElementPointSizeEv(const DomFont *self) {
  return self->hasElementPointSize();
}

//  void DomFont::clearElementPointSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont21clearElementPointSizeEv(DomFont *self) {
  self->clearElementPointSize();
}

//  int DomFont::elementWeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7DomFont13elementWeightEv(const DomFont *self) {
  return self->elementWeight();
}

//  void DomFont::setElementWeight(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont16setElementWeightEi(DomFont *self, int a) {
  self->setElementWeight(a);
}

//  bool DomFont::hasElementWeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont16hasElementWeightEv(const DomFont *self) {
  return self->hasElementWeight();
}

//  void DomFont::clearElementWeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont18clearElementWeightEv(DomFont *self) {
  self->clearElementWeight();
}

//  bool DomFont::elementItalic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont13elementItalicEv(const DomFont *self) {
  return self->elementItalic();
}

//  void DomFont::setElementItalic(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont16setElementItalicEb(DomFont *self, bool a) {
  self->setElementItalic(a);
}

//  bool DomFont::hasElementItalic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont16hasElementItalicEv(const DomFont *self) {
  return self->hasElementItalic();
}

//  void DomFont::clearElementItalic()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont18clearElementItalicEv(DomFont *self) {
  self->clearElementItalic();
}

//  bool DomFont::elementBold() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont11elementBoldEv(const DomFont *self) {
  return self->elementBold();
}

//  void DomFont::setElementBold(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont14setElementBoldEb(DomFont *self, bool a) {
  self->setElementBold(a);
}

//  bool DomFont::hasElementBold() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont14hasElementBoldEv(const DomFont *self) {
  return self->hasElementBold();
}

//  void DomFont::clearElementBold()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont16clearElementBoldEv(DomFont *self) {
  self->clearElementBold();
}

//  bool DomFont::elementUnderline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont16elementUnderlineEv(const DomFont *self) {
  return self->elementUnderline();
}

//  void DomFont::setElementUnderline(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont19setElementUnderlineEb(DomFont *self, bool a) {
  self->setElementUnderline(a);
}

//  bool DomFont::hasElementUnderline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont19hasElementUnderlineEv(const DomFont *self) {
  return self->hasElementUnderline();
}

//  void DomFont::clearElementUnderline()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont21clearElementUnderlineEv(DomFont *self) {
  self->clearElementUnderline();
}

//  bool DomFont::elementStrikeOut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont16elementStrikeOutEv(const DomFont *self) {
  return self->elementStrikeOut();
}

//  void DomFont::setElementStrikeOut(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont19setElementStrikeOutEb(DomFont *self, bool a) {
  self->setElementStrikeOut(a);
}

//  bool DomFont::hasElementStrikeOut() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont19hasElementStrikeOutEv(const DomFont *self) {
  return self->hasElementStrikeOut();
}

//  void DomFont::clearElementStrikeOut()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont21clearElementStrikeOutEv(DomFont *self) {
  self->clearElementStrikeOut();
}

//  bool DomFont::elementAntialiasing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont19elementAntialiasingEv(const DomFont *self) {
  return self->elementAntialiasing();
}

//  void DomFont::setElementAntialiasing(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont22setElementAntialiasingEb(DomFont *self, bool a) {
  self->setElementAntialiasing(a);
}

//  bool DomFont::hasElementAntialiasing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont22hasElementAntialiasingEv(const DomFont *self) {
  return self->hasElementAntialiasing();
}

//  void DomFont::clearElementAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont24clearElementAntialiasingEv(DomFont *self) {
  self->clearElementAntialiasing();
}

//  QString DomFont::elementStyleStrategy() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7DomFont20elementStyleStrategyEv(const DomFont *self) {
  return new QString(self->elementStyleStrategy());
}

//  void DomFont::setElementStyleStrategy(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont23setElementStyleStrategyERK7QString(
    DomFont *self,
    const QString *a) {
  self->setElementStyleStrategy(*a);
}

//  bool DomFont::hasElementStyleStrategy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont23hasElementStyleStrategyEv(const DomFont *self) {
  return self->hasElementStyleStrategy();
}

//  void DomFont::clearElementStyleStrategy()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont25clearElementStyleStrategyEv(DomFont *self) {
  self->clearElementStyleStrategy();
}

//  bool DomFont::elementKerning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont14elementKerningEv(const DomFont *self) {
  return self->elementKerning();
}

//  void DomFont::setElementKerning(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont17setElementKerningEb(DomFont *self, bool a) {
  self->setElementKerning(a);
}

//  bool DomFont::hasElementKerning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont17hasElementKerningEv(const DomFont *self) {
  return self->hasElementKerning();
}

//  void DomFont::clearElementKerning()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont19clearElementKerningEv(DomFont *self) {
  self->clearElementKerning();
}

//  QString DomFont::elementHintingPreference() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7DomFont24elementHintingPreferenceEv(
    const DomFont *self) {
  return new QString(self->elementHintingPreference());
}

//  void DomFont::setElementHintingPreference(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont27setElementHintingPreferenceERK7QString(
    DomFont *self,
    const QString *a) {
  self->setElementHintingPreference(*a);
}

//  bool DomFont::hasElementHintingPreference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont27hasElementHintingPreferenceEv(const DomFont *self) {
  return self->hasElementHintingPreference();
}

//  void DomFont::clearElementHintingPreference()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont29clearElementHintingPreferenceEv(DomFont *self) {
  self->clearElementHintingPreference();
}

//  QString DomFont::elementFontWeight() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7DomFont17elementFontWeightEv(const DomFont *self) {
  return new QString(self->elementFontWeight());
}

//  void DomFont::setElementFontWeight(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont20setElementFontWeightERK7QString(
    DomFont *self,
    const QString *a) {
  self->setElementFontWeight(*a);
}

//  bool DomFont::hasElementFontWeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomFont20hasElementFontWeightEv(const DomFont *self) {
  return self->hasElementFontWeight();
}

//  void DomFont::clearElementFontWeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomFont22clearElementFontWeightEv(DomFont *self) {
  self->clearElementFontWeight();
}
