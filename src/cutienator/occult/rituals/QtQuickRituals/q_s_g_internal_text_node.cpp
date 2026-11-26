//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsginternaltextnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsginternaltextnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qpoint.h>
#include <QtGui/qglyphrun.h>
#include <cstring>
#include <utility>

//  Only a class built on QSGInternalTextNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGInternalTextNode : QSGInternalTextNode {
  using QSGInternalTextNode::doAddTextLayout;
  using QSGInternalTextNode::doAddTextDocument;
};

//  A QSGInternalTextNode that Python can take functions over in. Every QSGInternalTextNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGInternalTextNodeCall0)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGInternalTextNodeCall1)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall2)(const void *, int, int *);
typedef int (*CuteQSGInternalTextNodeCall3)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall4)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGInternalTextNodeCall5)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall6)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGInternalTextNodeCall7)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall8)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGInternalTextNodeCall9)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall10)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGInternalTextNodeCall11)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall12)(const void *, int, int *);
typedef int (*CuteQSGInternalTextNodeCall13)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall14)(const void *, int, int *);
typedef int (*CuteQSGInternalTextNodeCall15)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall16)(const void *, int, int *);
typedef int (*CuteQSGInternalTextNodeCall17)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall18)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGInternalTextNodeCall19)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall20)(const void *, const QRectF *, const QColor *, int, QSGInternalTextNode::RecycleBin *, int *);
typedef void (*CuteQSGInternalTextNodeCall21)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall22)(const void *, const QPointF *, QTextLayout *, int, int, int, int, int *);
typedef void (*CuteQSGInternalTextNodeCall23)(const void *, const QPointF *, QTextDocument *, int, int, int *);
typedef bool (*CuteQSGInternalTextNodeCall24)(const void *, int *);
typedef void (*CuteQSGInternalTextNodeCall25)(const void *, int *);
class CuteQSGInternalTextNode : public QSGInternalTextNode {
public:
  using QSGInternalTextNode::QSGInternalTextNode;
  void *taken[26] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QSGTextNode8setColorE6QColor")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode5colorEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setTextStyleENS_9TextStyleE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode9textStyleEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode13setStyleColorE6QColor")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode10styleColorEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setLinkColorE6QColor")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode9linkColorEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode17setSelectionColorE6QColor")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode14selectionColorEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode21setSelectionTextColorE6QColor")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode18selectionTextColorEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode20setRenderTypeQualityEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode17renderTypeQualityEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode13setRenderTypeENS_10RenderTypeE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode10renderTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode9filteringEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode11setViewportERK6QRectF")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode8viewportEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGInternalTextNode17addDecorationNodeERK6QRectFRK6QColorN15QTextCharFormat14UnderlineStyleEPNS_10RecycleBinE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode5clearEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode17doAddTextDocumentE7QPointFP13QTextDocumentii")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[25] = call;
      return true;
    }
    return false;
  }

  //  void QSGInternalTextNode::setColor(QColor color)
  void setColor(QColor color) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall0 call = reinterpret_cast<CuteQSGInternalTextNodeCall0>(taken[0]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setColor(color);
  }

  //  QColor QSGInternalTextNode::color() const
  QColor color() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall1 call = reinterpret_cast<CuteQSGInternalTextNodeCall1>(taken[1]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::color();
  }

  //  void QSGInternalTextNode::setTextStyle(TextStyle textStyle)
  void setTextStyle(QSGTextNode::TextStyle textStyle) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall2 call = reinterpret_cast<CuteQSGInternalTextNodeCall2>(taken[2]);
      call(this, static_cast<int>(textStyle), &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setTextStyle(textStyle);
  }

  //  TextStyle QSGInternalTextNode::textStyle()
  QSGTextNode::TextStyle textStyle() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall3 call = reinterpret_cast<CuteQSGInternalTextNodeCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTextNode::TextStyle>(given);
    }
    return QSGInternalTextNode::textStyle();
  }

  //  void QSGInternalTextNode::setStyleColor(QColor styleColor)
  void setStyleColor(QColor styleColor) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall4 call = reinterpret_cast<CuteQSGInternalTextNodeCall4>(taken[4]);
      call(this, &styleColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setStyleColor(styleColor);
  }

  //  QColor QSGInternalTextNode::styleColor() const
  QColor styleColor() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall5 call = reinterpret_cast<CuteQSGInternalTextNodeCall5>(taken[5]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::styleColor();
  }

  //  void QSGInternalTextNode::setLinkColor(QColor linkColor)
  void setLinkColor(QColor linkColor) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall6 call = reinterpret_cast<CuteQSGInternalTextNodeCall6>(taken[6]);
      call(this, &linkColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setLinkColor(linkColor);
  }

  //  QColor QSGInternalTextNode::linkColor() const
  QColor linkColor() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall7 call = reinterpret_cast<CuteQSGInternalTextNodeCall7>(taken[7]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::linkColor();
  }

  //  void QSGInternalTextNode::setSelectionColor(QColor selectionColor)
  void setSelectionColor(QColor selectionColor) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall8 call = reinterpret_cast<CuteQSGInternalTextNodeCall8>(taken[8]);
      call(this, &selectionColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setSelectionColor(selectionColor);
  }

  //  QColor QSGInternalTextNode::selectionColor() const
  QColor selectionColor() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall9 call = reinterpret_cast<CuteQSGInternalTextNodeCall9>(taken[9]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::selectionColor();
  }

  //  void QSGInternalTextNode::setSelectionTextColor(QColor
  //      selectionTextColor)
  void setSelectionTextColor(QColor selectionTextColor) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall10 call = reinterpret_cast<CuteQSGInternalTextNodeCall10>(taken[10]);
      call(this, &selectionTextColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setSelectionTextColor(selectionTextColor);
  }

  //  QColor QSGInternalTextNode::selectionTextColor() const
  QColor selectionTextColor() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall11 call = reinterpret_cast<CuteQSGInternalTextNodeCall11>(taken[11]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::selectionTextColor();
  }

  //  void QSGInternalTextNode::setRenderTypeQuality(int renderTypeQuality)
  void setRenderTypeQuality(int renderTypeQuality) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall12 call = reinterpret_cast<CuteQSGInternalTextNodeCall12>(taken[12]);
      call(this, renderTypeQuality, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setRenderTypeQuality(renderTypeQuality);
  }

  //  int QSGInternalTextNode::renderTypeQuality() const
  int renderTypeQuality() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall13 call = reinterpret_cast<CuteQSGInternalTextNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGInternalTextNode::renderTypeQuality();
  }

  //  void QSGInternalTextNode::setRenderType(RenderType renderType)
  void setRenderType(QSGTextNode::RenderType renderType) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall14 call = reinterpret_cast<CuteQSGInternalTextNodeCall14>(taken[14]);
      call(this, static_cast<int>(renderType), &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setRenderType(renderType);
  }

  //  RenderType QSGInternalTextNode::renderType() const
  QSGTextNode::RenderType renderType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall15 call = reinterpret_cast<CuteQSGInternalTextNodeCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTextNode::RenderType>(given);
    }
    return QSGInternalTextNode::renderType();
  }

  //  void QSGInternalTextNode::setFiltering(QSGTexture::Filtering
  //      filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall16 call = reinterpret_cast<CuteQSGInternalTextNodeCall16>(taken[16]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setFiltering(filtering);
  }

  //  QSGTexture::Filtering QSGInternalTextNode::filtering() const
  QSGTexture::Filtering filtering() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall17 call = reinterpret_cast<CuteQSGInternalTextNodeCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return QSGInternalTextNode::filtering();
  }

  //  void QSGInternalTextNode::setViewport(const QRectF &viewport)
  void setViewport(const QRectF &viewport) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall18 call = reinterpret_cast<CuteQSGInternalTextNodeCall18>(taken[18]);
      call(this, &viewport, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setViewport(viewport);
  }

  //  QRectF QSGInternalTextNode::viewport() const
  QRectF viewport() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall19 call = reinterpret_cast<CuteQSGInternalTextNodeCall19>(taken[19]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::viewport();
  }

  //  void QSGInternalTextNode::addDecorationNode(const QRectF &rect, const
  //      QColor &color, QTextCharFormat::UnderlineStyle style, RecycleBin
  //      *recycleBin)
  void addDecorationNode(
      const QRectF &rect,
      const QColor &color,
      QTextCharFormat::UnderlineStyle style,
      QSGInternalTextNode::RecycleBin *recycleBin) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall20 call = reinterpret_cast<CuteQSGInternalTextNodeCall20>(taken[20]);
      call(this, &rect, &color, static_cast<int>(style), recycleBin, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::addDecorationNode(rect, color, style, recycleBin);
  }

  //  void QSGInternalTextNode::clear()
  void clear() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall21 call = reinterpret_cast<CuteQSGInternalTextNodeCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::clear();
  }

  //  void QSGInternalTextNode::doAddTextLayout(QPointF position,
  //      QTextLayout *textLayout, int selectionStart, int selectionEnd,
  //      int lineStart, int lineCount)
  void doAddTextLayout(
      QPointF position,
      QTextLayout *textLayout,
      int selectionStart,
      int selectionEnd,
      int lineStart,
      int lineCount) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall22 call = reinterpret_cast<CuteQSGInternalTextNodeCall22>(taken[22]);
      call(this, &position, textLayout, selectionStart, selectionEnd, lineStart, lineCount, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::doAddTextLayout(position, textLayout, selectionStart, selectionEnd, lineStart, lineCount);
  }

  //  void QSGInternalTextNode::doAddTextDocument(QPointF position,
  //      QTextDocument *textDocument, int selectionStart, int
  //      selectionEnd)
  void doAddTextDocument(
      QPointF position,
      QTextDocument *textDocument,
      int selectionStart,
      int selectionEnd) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall23 call = reinterpret_cast<CuteQSGInternalTextNodeCall23>(taken[23]);
      call(this, &position, textDocument, selectionStart, selectionEnd, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::doAddTextDocument(position, textDocument, selectionStart, selectionEnd);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall24 call = reinterpret_cast<CuteQSGInternalTextNodeCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGInternalTextNodeCall25 call = reinterpret_cast<CuteQSGInternalTextNodeCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGInternalTextNode::QSGInternalTextNode(QSGRenderContext *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalTextNode *ritual_ZN19QSGInternalTextNodeC1EP16QSGRenderContext(
    QSGRenderContext *renderContext) {
  return new CuteQSGInternalTextNode(renderContext);
}

//  QSGInternalTextNode::~QSGInternalTextNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNodeD1Ev(QSGInternalTextNode *self) {
  delete self;
}

//  void QSGInternalTextNode::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode8setColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QSGInternalTextNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QSGInternalTextNode5colorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->color());
}

//  void QSGInternalTextNode::setTextStyle(TextStyle textStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode12setTextStyleEN11QSGTextNode9TextStyleE(
    QSGInternalTextNode *self,
    QSGTextNode::TextStyle textStyle) {
  self->setTextStyle(textStyle);
}

//  TextStyle QSGInternalTextNode::textStyle()
extern "C" Q_DECL_EXPORT
QSGTextNode::TextStyle ritual_ZN19QSGInternalTextNode9textStyleEv(
    QSGInternalTextNode *self) {
  return self->textStyle();
}

//  void QSGInternalTextNode::setStyleColor(QColor styleColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode13setStyleColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *styleColor) {
  self->setStyleColor(*styleColor);
}

//  QColor QSGInternalTextNode::styleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QSGInternalTextNode10styleColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->styleColor());
}

//  void QSGInternalTextNode::setLinkColor(QColor linkColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode12setLinkColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *linkColor) {
  self->setLinkColor(*linkColor);
}

//  QColor QSGInternalTextNode::linkColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QSGInternalTextNode9linkColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->linkColor());
}

//  void QSGInternalTextNode::setSelectionColor(QColor selectionColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode17setSelectionColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *selectionColor) {
  self->setSelectionColor(*selectionColor);
}

//  QColor QSGInternalTextNode::selectionColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QSGInternalTextNode14selectionColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->selectionColor());
}

//  void QSGInternalTextNode::setSelectionTextColor(QColor
//      selectionTextColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode21setSelectionTextColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *selectionTextColor) {
  self->setSelectionTextColor(*selectionTextColor);
}

//  QColor QSGInternalTextNode::selectionTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QSGInternalTextNode18selectionTextColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->selectionTextColor());
}

//  void QSGInternalTextNode::setRenderTypeQuality(int renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode20setRenderTypeQualityEi(
    QSGInternalTextNode *self,
    int renderTypeQuality) {
  self->setRenderTypeQuality(renderTypeQuality);
}

//  int QSGInternalTextNode::renderTypeQuality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSGInternalTextNode17renderTypeQualityEv(
    const QSGInternalTextNode *self) {
  return self->renderTypeQuality();
}

//  void QSGInternalTextNode::setRenderType(RenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode13setRenderTypeEN11QSGTextNode10RenderTypeE(
    QSGInternalTextNode *self,
    QSGTextNode::RenderType renderType) {
  self->setRenderType(renderType);
}

//  RenderType QSGInternalTextNode::renderType() const
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_ZNK19QSGInternalTextNode10renderTypeEv(
    const QSGInternalTextNode *self) {
  return self->renderType();
}

//  bool QSGInternalTextNode::containsUnscalableGlyphs() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSGInternalTextNode24containsUnscalableGlyphsEv(
    const QSGInternalTextNode *self) {
  return self->containsUnscalableGlyphs();
}

//  void QSGInternalTextNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode12setFilteringEN10QSGTexture9FilteringE(
    QSGInternalTextNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  QSGTexture::Filtering QSGInternalTextNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK19QSGInternalTextNode9filteringEv(
    const QSGInternalTextNode *self) {
  return self->filtering();
}

//  void QSGInternalTextNode::setViewport(const QRectF &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode11setViewportERK6QRectF(
    QSGInternalTextNode *self,
    const QRectF *viewport) {
  self->setViewport(*viewport);
}

//  QRectF QSGInternalTextNode::viewport() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QSGInternalTextNode8viewportEv(
    const QSGInternalTextNode *self) {
  return new QRectF(self->viewport());
}

//  void QSGInternalTextNode::setDevicePixelRatio(qreal dpr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode19setDevicePixelRatioEd(
    QSGInternalTextNode *self,
    qreal dpr) {
  self->setDevicePixelRatio(dpr);
}

//  void QSGInternalTextNode::setCursor(const QRectF &rect, const QColor
//      &color, RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode9setCursorERK6QRectFRK6QColorPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    const QRectF *rect,
    const QColor *color,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->setCursor(*rect, *color, recycleBin);
}

//  void QSGInternalTextNode::clearCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode11clearCursorEv(
    QSGInternalTextNode *self) {
  self->clearCursor();
}

//  void QSGInternalTextNode::addRectangleNode(const QRectF &rect, const
//      QColor &color, RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode16addRectangleNodeERK6QRectFRK6QColorPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    const QRectF *rect,
    const QColor *color,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->addRectangleNode(*rect, *color, recycleBin);
}

//  void QSGInternalTextNode::addDecorationNode(const QRectF &rect, const
//      QColor &color, QTextCharFormat::UnderlineStyle style, RecycleBin
//      *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode17addDecorationNodeERK6QRectFRK6QColorN15QTextCharFormat14UnderlineStyleEPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    const QRectF *rect,
    const QColor *color,
    QTextCharFormat::UnderlineStyle style,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->addDecorationNode(*rect, *color, style, recycleBin);
}

//  void QSGInternalTextNode::addImage(const QRectF &rect, const QImage
//      &image, RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode8addImageERK6QRectFRK6QImagePNS_10RecycleBinE(
    QSGInternalTextNode *self,
    const QRectF *rect,
    const QImage *image,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->addImage(*rect, *image, recycleBin);
}

//  void QSGInternalTextNode::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode5clearEv(QSGInternalTextNode *self) {
  self->clear();
}

//  void QSGInternalTextNode::recycle(RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode7recycleEPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->recycle(recycleBin);
}

//  QSGGlyphNode *QSGInternalTextNode::addGlyphs(const QPointF &position,
//      const QGlyphRun &glyphs, const QColor &color, RecycleBin *recycleBin,
//      QQuickText::TextStyle style, const QColor &styleColor, QSGNode
//      *parentNode)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_ZN19QSGInternalTextNode9addGlyphsERK7QPointFRK9QGlyphRunRK6QColorPNS_10RecycleBinEN10QQuickText9TextStyleES8_P7QSGNode(
    QSGInternalTextNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs,
    const QColor *color,
    QSGInternalTextNode::RecycleBin *recycleBin,
    QQuickText::TextStyle style,
    const QColor *styleColor,
    QSGNode *parentNode) {
  return self->addGlyphs(
      *position,
      *glyphs,
      *color,
      recycleBin,
      style,
      *styleColor,
      parentNode);
}

//  QSGInternalRectangleNode *QSGInternalTextNode::cursorNode() const
extern "C" Q_DECL_EXPORT
QSGInternalRectangleNode *ritual_ZNK19QSGInternalTextNode10cursorNodeEv(
    const QSGInternalTextNode *self) {
  return self->cursorNode();
}

//  std::pair<int, int> QSGInternalTextNode::renderedLineRange() const
extern "C" Q_DECL_EXPORT
std::pair<int, int> *ritual_ZNK19QSGInternalTextNode17renderedLineRangeEv(
    const QSGInternalTextNode *self) {
  return new std::pair<int, int>(self->renderedLineRange());
}

//  void QSGInternalTextNode::discardUnusedNodes(RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode18discardUnusedNodesEPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->discardUnusedNodes(recycleBin);
}

//  void QSGInternalTextNode::addTextLayout(QPointF position, QTextLayout
//      *layout, RecycleBin *recycleBin, int selectionStart, int
//      selectionCount, int lineStart, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode13addTextLayoutE7QPointFP11QTextLayoutPNS_10RecycleBinEiiii(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextLayout *layout,
    QSGInternalTextNode::RecycleBin *recycleBin,
    int selectionStart,
    int selectionCount,
    int lineStart,
    int lineCount) {
  self->addTextLayout(
      *position,
      layout,
      recycleBin,
      selectionStart,
      selectionCount,
      lineStart,
      lineCount);
}

//  void QSGInternalTextNode::addTextDocument(QPointF position, QTextDocument
//      *document, RecycleBin *recycleBin, int selectionStart, int
//      selectionCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode15addTextDocumentE7QPointFP13QTextDocumentPNS_10RecycleBinEii(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextDocument *document,
    QSGInternalTextNode::RecycleBin *recycleBin,
    int selectionStart,
    int selectionCount) {
  self->addTextDocument(
      *position,
      document,
      recycleBin,
      selectionStart,
      selectionCount);
}

//  void QSGInternalTextNode::doAddTextLayout(QPointF position, QTextLayout
//      *textLayout, int selectionStart, int selectionEnd, int lineStart, int
//      lineCount, RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiiiPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextLayout *textLayout,
    int selectionStart,
    int selectionEnd,
    int lineStart,
    int lineCount,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->doAddTextLayout(
      *position,
      textLayout,
      selectionStart,
      selectionEnd,
      lineStart,
      lineCount,
      recycleBin);
}

//  void QSGInternalTextNode::doAddTextLayout(QPointF position, QTextLayout
//      *textLayout, int selectionStart, int selectionEnd, int lineStart, int
//      lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextLayout *textLayout,
    int selectionStart,
    int selectionEnd,
    int lineStart,
    int lineCount) {
  self->doAddTextLayout(
      *position,
      textLayout,
      selectionStart,
      selectionEnd,
      lineStart,
      lineCount);
}

//  void QSGInternalTextNode::doAddTextDocument(QPointF position,
//      QTextDocument *textDocument, int selectionStart, int selectionEnd,
//      RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode17doAddTextDocumentE7QPointFP13QTextDocumentiiPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextDocument *textDocument,
    int selectionStart,
    int selectionEnd,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->doAddTextDocument(
      *position,
      textDocument,
      selectionStart,
      selectionEnd,
      recycleBin);
}

//  void QSGInternalTextNode::doAddTextDocument(QPointF position,
//      QTextDocument *textDocument, int selectionStart, int selectionEnd)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGInternalTextNode17doAddTextDocumentE7QPointFP13QTextDocumentii(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextDocument *textDocument,
    int selectionStart,
    int selectionEnd) {
  self->doAddTextDocument(
      *position,
      textDocument,
      selectionStart,
      selectionEnd);
}

//  QSGInternalImageNode
//      *QSGInternalTextNode::findOrCreateImageNode(RecycleBin *recycleBin)
extern "C" Q_DECL_EXPORT
QSGInternalImageNode *ritual_ZN19QSGInternalTextNode21findOrCreateImageNodeEPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  return self->findOrCreateImageNode(recycleBin);
}

//  QSGGlyphNode *QSGInternalTextNode::findOrCreateGlyphNode(RenderType
//      renderType, RecycleBin *recycleBin, QSGNode *parentNode)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_ZN19QSGInternalTextNode21findOrCreateGlyphNodeEN11QSGTextNode10RenderTypeEPNS_10RecycleBinEP7QSGNode(
    QSGInternalTextNode *self,
    QSGTextNode::RenderType renderType,
    QSGInternalTextNode::RecycleBin *recycleBin,
    QSGNode *parentNode) {
  return self->findOrCreateGlyphNode(renderType, recycleBin, parentNode);
}

//  QSGInternalRectangleNode
//      *QSGInternalTextNode::findOrCreateRectangleNode(RecycleBin
//      *recycleBin)
extern "C" Q_DECL_EXPORT
QSGInternalRectangleNode *ritual_ZN19QSGInternalTextNode25findOrCreateRectangleNodeEPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  return self->findOrCreateRectangleNode(recycleBin);
}

//  a Python function taken by a CuteQSGInternalTextNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGInternalTextNode(
    QSGInternalTextNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGInternalTextNode *>(self)->take(key, call);
}

//  void QSGInternalTextNode::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode8setColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *color) {
  self->QSGInternalTextNode::setColor(*color);
}

//  QColor QSGInternalTextNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK19QSGInternalTextNode5colorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->QSGInternalTextNode::color());
}

//  void QSGInternalTextNode::setTextStyle(TextStyle textStyle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode12setTextStyleEN11QSGTextNode9TextStyleE(
    QSGInternalTextNode *self,
    QSGTextNode::TextStyle textStyle) {
  self->QSGInternalTextNode::setTextStyle(textStyle);
}

//  TextStyle QSGInternalTextNode::textStyle()
extern "C" Q_DECL_EXPORT
QSGTextNode::TextStyle ritual_own_ZN19QSGInternalTextNode9textStyleEv(
    QSGInternalTextNode *self) {
  return self->QSGInternalTextNode::textStyle();
}

//  void QSGInternalTextNode::setStyleColor(QColor styleColor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode13setStyleColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *styleColor) {
  self->QSGInternalTextNode::setStyleColor(*styleColor);
}

//  QColor QSGInternalTextNode::styleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK19QSGInternalTextNode10styleColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->QSGInternalTextNode::styleColor());
}

//  void QSGInternalTextNode::setLinkColor(QColor linkColor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode12setLinkColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *linkColor) {
  self->QSGInternalTextNode::setLinkColor(*linkColor);
}

//  QColor QSGInternalTextNode::linkColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK19QSGInternalTextNode9linkColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->QSGInternalTextNode::linkColor());
}

//  void QSGInternalTextNode::setSelectionColor(QColor selectionColor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode17setSelectionColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *selectionColor) {
  self->QSGInternalTextNode::setSelectionColor(*selectionColor);
}

//  QColor QSGInternalTextNode::selectionColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK19QSGInternalTextNode14selectionColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->QSGInternalTextNode::selectionColor());
}

//  void QSGInternalTextNode::setSelectionTextColor(QColor
//      selectionTextColor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode21setSelectionTextColorE6QColor(
    QSGInternalTextNode *self,
    const QColor *selectionTextColor) {
  self->QSGInternalTextNode::setSelectionTextColor(*selectionTextColor);
}

//  QColor QSGInternalTextNode::selectionTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK19QSGInternalTextNode18selectionTextColorEv(
    const QSGInternalTextNode *self) {
  return new QColor(self->QSGInternalTextNode::selectionTextColor());
}

//  void QSGInternalTextNode::setRenderTypeQuality(int renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode20setRenderTypeQualityEi(
    QSGInternalTextNode *self,
    int renderTypeQuality) {
  self->QSGInternalTextNode::setRenderTypeQuality(renderTypeQuality);
}

//  int QSGInternalTextNode::renderTypeQuality() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QSGInternalTextNode17renderTypeQualityEv(
    const QSGInternalTextNode *self) {
  return self->QSGInternalTextNode::renderTypeQuality();
}

//  void QSGInternalTextNode::setRenderType(RenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode13setRenderTypeEN11QSGTextNode10RenderTypeE(
    QSGInternalTextNode *self,
    QSGTextNode::RenderType renderType) {
  self->QSGInternalTextNode::setRenderType(renderType);
}

//  RenderType QSGInternalTextNode::renderType() const
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_own_ZNK19QSGInternalTextNode10renderTypeEv(
    const QSGInternalTextNode *self) {
  return self->QSGInternalTextNode::renderType();
}

//  void QSGInternalTextNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode12setFilteringEN10QSGTexture9FilteringE(
    QSGInternalTextNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGInternalTextNode::setFiltering(filtering);
}

//  QSGTexture::Filtering QSGInternalTextNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_own_ZNK19QSGInternalTextNode9filteringEv(
    const QSGInternalTextNode *self) {
  return self->QSGInternalTextNode::filtering();
}

//  void QSGInternalTextNode::setViewport(const QRectF &viewport)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode11setViewportERK6QRectF(
    QSGInternalTextNode *self,
    const QRectF *viewport) {
  self->QSGInternalTextNode::setViewport(*viewport);
}

//  QRectF QSGInternalTextNode::viewport() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QSGInternalTextNode8viewportEv(
    const QSGInternalTextNode *self) {
  return new QRectF(self->QSGInternalTextNode::viewport());
}

//  void QSGInternalTextNode::addDecorationNode(const QRectF &rect, const
//      QColor &color, QTextCharFormat::UnderlineStyle style, RecycleBin
//      *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode17addDecorationNodeERK6QRectFRK6QColorN15QTextCharFormat14UnderlineStyleEPNS_10RecycleBinE(
    QSGInternalTextNode *self,
    const QRectF *rect,
    const QColor *color,
    QTextCharFormat::UnderlineStyle style,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->QSGInternalTextNode::addDecorationNode(
      *rect,
      *color,
      style,
      recycleBin);
}

//  void QSGInternalTextNode::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode5clearEv(QSGInternalTextNode *self) {
  self->QSGInternalTextNode::clear();
}

//  void QSGInternalTextNode::doAddTextLayout(QPointF position, QTextLayout
//      *textLayout, int selectionStart, int selectionEnd, int lineStart, int
//      lineCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextLayout *textLayout,
    int selectionStart,
    int selectionEnd,
    int lineStart,
    int lineCount) {
  static_cast<OwnQSGInternalTextNode *>(self)->OwnQSGInternalTextNode::doAddTextLayout(
      *position,
      textLayout,
      selectionStart,
      selectionEnd,
      lineStart,
      lineCount);
}

//  void QSGInternalTextNode::doAddTextDocument(QPointF position,
//      QTextDocument *textDocument, int selectionStart, int selectionEnd)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGInternalTextNode17doAddTextDocumentE7QPointFP13QTextDocumentii(
    QSGInternalTextNode *self,
    const QPointF *position,
    QTextDocument *textDocument,
    int selectionStart,
    int selectionEnd) {
  static_cast<OwnQSGInternalTextNode *>(self)->OwnQSGInternalTextNode::doAddTextDocument(
      *position,
      textDocument,
      selectionStart,
      selectionEnd);
}

//  a std::pair<int, int> a ritual of QSGInternalTextNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSGInternalTextNode__std_pair_int_int(
    std::pair<int, int> *self) {
  delete self;
}
