//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgvisitor_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QSvgVisitor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSvgVisitor : QSvgVisitor {
  using QSvgVisitor::visitNode;
  using QSvgVisitor::visitStructureNodeStart;
  using QSvgVisitor::visitStructureNodeEnd;
  using QSvgVisitor::visitAnimateNode;
  using QSvgVisitor::visitEllipseNode;
  using QSvgVisitor::visitImageNode;
  using QSvgVisitor::visitLineNode;
  using QSvgVisitor::visitPathNode;
  using QSvgVisitor::visitPolygonNode;
  using QSvgVisitor::visitPolylineNode;
  using QSvgVisitor::visitRectNode;
  using QSvgVisitor::visitTextNode;
  using QSvgVisitor::visitTspanNode;
  using QSvgVisitor::visitUseNode;
  using QSvgVisitor::visitVideoNode;
  using QSvgVisitor::visitDocumentNodeStart;
  using QSvgVisitor::visitDocumentNodeEnd;
  using QSvgVisitor::visitGroupNodeStart;
  using QSvgVisitor::visitGroupNodeEnd;
  using QSvgVisitor::visitDefsNodeStart;
  using QSvgVisitor::visitDefsNodeEnd;
  using QSvgVisitor::visitSwitchNodeStart;
  using QSvgVisitor::visitSwitchNodeEnd;
  using QSvgVisitor::visitMaskNodeStart;
  using QSvgVisitor::visitMaskNodeEnd;
  using QSvgVisitor::visitSymbolNodeStart;
  using QSvgVisitor::visitSymbolNodeEnd;
  using QSvgVisitor::visitMarkerNodeStart;
  using QSvgVisitor::visitMarkerNodeEnd;
  using QSvgVisitor::visitPatternNodeStart;
  using QSvgVisitor::visitPatternNodeEnd;
  using QSvgVisitor::visitFilterNodeStart;
  using QSvgVisitor::visitFilterNodeEnd;
  using QSvgVisitor::visitFeFilterPrimitiveNodeStart;
  using QSvgVisitor::visitFeFilterPrimitiveNodeEnd;
};

//  A QSvgVisitor that Python can take functions over in. Every QSvgVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSvgVisitorCall0)(const void *, const QSvgStructureNode *, int *);
typedef void (*CuteQSvgVisitorCall1)(const void *, const QSvgNode *, int *);
typedef void (*CuteQSvgVisitorCall2)(const void *, const QSvgNode *, int *);
typedef bool (*CuteQSvgVisitorCall3)(const void *, const QSvgStructureNode *, int *);
typedef void (*CuteQSvgVisitorCall4)(const void *, const QSvgStructureNode *, int *);
typedef void (*CuteQSvgVisitorCall5)(const void *, const QSvgAnimateNode *, int *);
typedef void (*CuteQSvgVisitorCall6)(const void *, const QSvgEllipse *, int *);
typedef void (*CuteQSvgVisitorCall7)(const void *, const QSvgImage *, int *);
typedef void (*CuteQSvgVisitorCall8)(const void *, const QSvgLine *, int *);
typedef void (*CuteQSvgVisitorCall9)(const void *, const QSvgPath *, int *);
typedef void (*CuteQSvgVisitorCall10)(const void *, const QSvgPolygon *, int *);
typedef void (*CuteQSvgVisitorCall11)(const void *, const QSvgPolyline *, int *);
typedef void (*CuteQSvgVisitorCall12)(const void *, const QSvgRect *, int *);
typedef void (*CuteQSvgVisitorCall13)(const void *, const QSvgText *, int *);
typedef void (*CuteQSvgVisitorCall14)(const void *, const QSvgTspan *, int *);
typedef void (*CuteQSvgVisitorCall15)(const void *, const QSvgUse *, int *);
typedef void (*CuteQSvgVisitorCall16)(const void *, const QSvgVideo *, int *);
typedef bool (*CuteQSvgVisitorCall17)(const void *, const QSvgDocument *, int *);
typedef void (*CuteQSvgVisitorCall18)(const void *, const QSvgDocument *, int *);
typedef bool (*CuteQSvgVisitorCall19)(const void *, const QSvgG *, int *);
typedef void (*CuteQSvgVisitorCall20)(const void *, const QSvgG *, int *);
typedef bool (*CuteQSvgVisitorCall21)(const void *, const QSvgDefs *, int *);
typedef void (*CuteQSvgVisitorCall22)(const void *, const QSvgDefs *, int *);
typedef bool (*CuteQSvgVisitorCall23)(const void *, const QSvgSwitch *, int *);
typedef void (*CuteQSvgVisitorCall24)(const void *, const QSvgSwitch *, int *);
typedef bool (*CuteQSvgVisitorCall25)(const void *, const QSvgMask *, int *);
typedef void (*CuteQSvgVisitorCall26)(const void *, const QSvgMask *, int *);
typedef bool (*CuteQSvgVisitorCall27)(const void *, const QSvgSymbol *, int *);
typedef void (*CuteQSvgVisitorCall28)(const void *, const QSvgSymbol *, int *);
typedef bool (*CuteQSvgVisitorCall29)(const void *, const QSvgMarker *, int *);
typedef void (*CuteQSvgVisitorCall30)(const void *, const QSvgMarker *, int *);
typedef bool (*CuteQSvgVisitorCall31)(const void *, const QSvgPattern *, int *);
typedef void (*CuteQSvgVisitorCall32)(const void *, const QSvgPattern *, int *);
typedef bool (*CuteQSvgVisitorCall33)(const void *, const QSvgFilterContainer *, int *);
typedef void (*CuteQSvgVisitorCall34)(const void *, const QSvgFilterContainer *, int *);
typedef bool (*CuteQSvgVisitorCall35)(const void *, const QSvgFeFilterPrimitive *, int *);
typedef void (*CuteQSvgVisitorCall36)(const void *, const QSvgFeFilterPrimitive *, int *);
class CuteQSvgVisitor : public QSvgVisitor {
public:
  using QSvgVisitor::QSvgVisitor;
  void *taken[37] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QSvgVisitor8traverseEPK17QSvgStructureNode")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor8traverseEPK8QSvgNode")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor9visitNodeEPK8QSvgNode")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor23visitStructureNodeStartEPK17QSvgStructureNode")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor21visitStructureNodeEndEPK17QSvgStructureNode")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor16visitAnimateNodeEPK15QSvgAnimateNode")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor16visitEllipseNodeEPK11QSvgEllipse")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor14visitImageNodeEPK9QSvgImage")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor13visitLineNodeEPK8QSvgLine")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor13visitPathNodeEPK8QSvgPath")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor16visitPolygonNodeEPK11QSvgPolygon")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor17visitPolylineNodeEPK12QSvgPolyline")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor13visitRectNodeEPK8QSvgRect")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor13visitTextNodeEPK8QSvgText")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor14visitTspanNodeEPK9QSvgTspan")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor12visitUseNodeEPK7QSvgUse")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor14visitVideoNodeEPK9QSvgVideo")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor22visitDocumentNodeStartEPK12QSvgDocument")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor20visitDocumentNodeEndEPK12QSvgDocument")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor19visitGroupNodeStartEPK5QSvgG")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor17visitGroupNodeEndEPK5QSvgG")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor18visitDefsNodeStartEPK8QSvgDefs")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor16visitDefsNodeEndEPK8QSvgDefs")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor20visitSwitchNodeStartEPK10QSvgSwitch")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor18visitSwitchNodeEndEPK10QSvgSwitch")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor18visitMaskNodeStartEPK8QSvgMask")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor16visitMaskNodeEndEPK8QSvgMask")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor20visitSymbolNodeStartEPK10QSvgSymbol")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor18visitSymbolNodeEndEPK10QSvgSymbol")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor20visitMarkerNodeStartEPK10QSvgMarker")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor18visitMarkerNodeEndEPK10QSvgMarker")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor21visitPatternNodeStartEPK11QSvgPattern")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor19visitPatternNodeEndEPK11QSvgPattern")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor20visitFilterNodeStartEPK19QSvgFilterContainer")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor18visitFilterNodeEndEPK19QSvgFilterContainer")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor31visitFeFilterPrimitiveNodeStartEPK21QSvgFeFilterPrimitive")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSvgVisitor29visitFeFilterPrimitiveNodeEndEPK21QSvgFeFilterPrimitive")) {
      taken[36] = call;
      return true;
    }
    return false;
  }

  //  void QSvgVisitor::traverse(const QSvgStructureNode *node)
  void traverse(const QSvgStructureNode *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgVisitorCall0 call = reinterpret_cast<CuteQSvgVisitorCall0>(taken[0]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::traverse(node);
  }

  //  void QSvgVisitor::traverse(const QSvgNode *node)
  void traverse(const QSvgNode *node) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgVisitorCall1 call = reinterpret_cast<CuteQSvgVisitorCall1>(taken[1]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::traverse(node);
  }

  //  void QSvgVisitor::visitNode(const QSvgNode *a0)
  void visitNode(const QSvgNode *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgVisitorCall2 call = reinterpret_cast<CuteQSvgVisitorCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitNode(a0);
  }

  //  bool QSvgVisitor::visitStructureNodeStart(const QSvgStructureNode
  //      *node)
  bool visitStructureNodeStart(const QSvgStructureNode *node) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgVisitorCall3 call = reinterpret_cast<CuteQSvgVisitorCall3>(taken[3]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitStructureNodeStart(node);
  }

  //  void QSvgVisitor::visitStructureNodeEnd(const QSvgStructureNode *a0)
  void visitStructureNodeEnd(const QSvgStructureNode *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSvgVisitorCall4 call = reinterpret_cast<CuteQSvgVisitorCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitStructureNodeEnd(a0);
  }

  //  void QSvgVisitor::visitAnimateNode(const QSvgAnimateNode *node)
  void visitAnimateNode(const QSvgAnimateNode *node) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSvgVisitorCall5 call = reinterpret_cast<CuteQSvgVisitorCall5>(taken[5]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitAnimateNode(node);
  }

  //  void QSvgVisitor::visitEllipseNode(const QSvgEllipse *node)
  void visitEllipseNode(const QSvgEllipse *node) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSvgVisitorCall6 call = reinterpret_cast<CuteQSvgVisitorCall6>(taken[6]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitEllipseNode(node);
  }

  //  void QSvgVisitor::visitImageNode(const QSvgImage *node)
  void visitImageNode(const QSvgImage *node) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSvgVisitorCall7 call = reinterpret_cast<CuteQSvgVisitorCall7>(taken[7]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitImageNode(node);
  }

  //  void QSvgVisitor::visitLineNode(const QSvgLine *node)
  void visitLineNode(const QSvgLine *node) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSvgVisitorCall8 call = reinterpret_cast<CuteQSvgVisitorCall8>(taken[8]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitLineNode(node);
  }

  //  void QSvgVisitor::visitPathNode(const QSvgPath *node)
  void visitPathNode(const QSvgPath *node) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSvgVisitorCall9 call = reinterpret_cast<CuteQSvgVisitorCall9>(taken[9]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitPathNode(node);
  }

  //  void QSvgVisitor::visitPolygonNode(const QSvgPolygon *node)
  void visitPolygonNode(const QSvgPolygon *node) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSvgVisitorCall10 call = reinterpret_cast<CuteQSvgVisitorCall10>(taken[10]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitPolygonNode(node);
  }

  //  void QSvgVisitor::visitPolylineNode(const QSvgPolyline *node)
  void visitPolylineNode(const QSvgPolyline *node) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSvgVisitorCall11 call = reinterpret_cast<CuteQSvgVisitorCall11>(taken[11]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitPolylineNode(node);
  }

  //  void QSvgVisitor::visitRectNode(const QSvgRect *node)
  void visitRectNode(const QSvgRect *node) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSvgVisitorCall12 call = reinterpret_cast<CuteQSvgVisitorCall12>(taken[12]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitRectNode(node);
  }

  //  void QSvgVisitor::visitTextNode(const QSvgText *node)
  void visitTextNode(const QSvgText *node) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSvgVisitorCall13 call = reinterpret_cast<CuteQSvgVisitorCall13>(taken[13]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitTextNode(node);
  }

  //  void QSvgVisitor::visitTspanNode(const QSvgTspan *node)
  void visitTspanNode(const QSvgTspan *node) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSvgVisitorCall14 call = reinterpret_cast<CuteQSvgVisitorCall14>(taken[14]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitTspanNode(node);
  }

  //  void QSvgVisitor::visitUseNode(const QSvgUse *node)
  void visitUseNode(const QSvgUse *node) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSvgVisitorCall15 call = reinterpret_cast<CuteQSvgVisitorCall15>(taken[15]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitUseNode(node);
  }

  //  void QSvgVisitor::visitVideoNode(const QSvgVideo *node)
  void visitVideoNode(const QSvgVideo *node) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSvgVisitorCall16 call = reinterpret_cast<CuteQSvgVisitorCall16>(taken[16]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitVideoNode(node);
  }

  //  bool QSvgVisitor::visitDocumentNodeStart(const QSvgDocument *node)
  bool visitDocumentNodeStart(const QSvgDocument *node) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSvgVisitorCall17 call = reinterpret_cast<CuteQSvgVisitorCall17>(taken[17]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitDocumentNodeStart(node);
  }

  //  void QSvgVisitor::visitDocumentNodeEnd(const QSvgDocument *node)
  void visitDocumentNodeEnd(const QSvgDocument *node) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSvgVisitorCall18 call = reinterpret_cast<CuteQSvgVisitorCall18>(taken[18]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitDocumentNodeEnd(node);
  }

  //  bool QSvgVisitor::visitGroupNodeStart(const QSvgG *node)
  bool visitGroupNodeStart(const QSvgG *node) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSvgVisitorCall19 call = reinterpret_cast<CuteQSvgVisitorCall19>(taken[19]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitGroupNodeStart(node);
  }

  //  void QSvgVisitor::visitGroupNodeEnd(const QSvgG *node)
  void visitGroupNodeEnd(const QSvgG *node) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSvgVisitorCall20 call = reinterpret_cast<CuteQSvgVisitorCall20>(taken[20]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitGroupNodeEnd(node);
  }

  //  bool QSvgVisitor::visitDefsNodeStart(const QSvgDefs *node)
  bool visitDefsNodeStart(const QSvgDefs *node) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSvgVisitorCall21 call = reinterpret_cast<CuteQSvgVisitorCall21>(taken[21]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitDefsNodeStart(node);
  }

  //  void QSvgVisitor::visitDefsNodeEnd(const QSvgDefs *node)
  void visitDefsNodeEnd(const QSvgDefs *node) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSvgVisitorCall22 call = reinterpret_cast<CuteQSvgVisitorCall22>(taken[22]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitDefsNodeEnd(node);
  }

  //  bool QSvgVisitor::visitSwitchNodeStart(const QSvgSwitch *node)
  bool visitSwitchNodeStart(const QSvgSwitch *node) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSvgVisitorCall23 call = reinterpret_cast<CuteQSvgVisitorCall23>(taken[23]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitSwitchNodeStart(node);
  }

  //  void QSvgVisitor::visitSwitchNodeEnd(const QSvgSwitch *node)
  void visitSwitchNodeEnd(const QSvgSwitch *node) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSvgVisitorCall24 call = reinterpret_cast<CuteQSvgVisitorCall24>(taken[24]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitSwitchNodeEnd(node);
  }

  //  bool QSvgVisitor::visitMaskNodeStart(const QSvgMask *node)
  bool visitMaskNodeStart(const QSvgMask *node) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSvgVisitorCall25 call = reinterpret_cast<CuteQSvgVisitorCall25>(taken[25]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitMaskNodeStart(node);
  }

  //  void QSvgVisitor::visitMaskNodeEnd(const QSvgMask *node)
  void visitMaskNodeEnd(const QSvgMask *node) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSvgVisitorCall26 call = reinterpret_cast<CuteQSvgVisitorCall26>(taken[26]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitMaskNodeEnd(node);
  }

  //  bool QSvgVisitor::visitSymbolNodeStart(const QSvgSymbol *node)
  bool visitSymbolNodeStart(const QSvgSymbol *node) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSvgVisitorCall27 call = reinterpret_cast<CuteQSvgVisitorCall27>(taken[27]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitSymbolNodeStart(node);
  }

  //  void QSvgVisitor::visitSymbolNodeEnd(const QSvgSymbol *node)
  void visitSymbolNodeEnd(const QSvgSymbol *node) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSvgVisitorCall28 call = reinterpret_cast<CuteQSvgVisitorCall28>(taken[28]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitSymbolNodeEnd(node);
  }

  //  bool QSvgVisitor::visitMarkerNodeStart(const QSvgMarker *a0)
  bool visitMarkerNodeStart(const QSvgMarker *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSvgVisitorCall29 call = reinterpret_cast<CuteQSvgVisitorCall29>(taken[29]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitMarkerNodeStart(a0);
  }

  //  void QSvgVisitor::visitMarkerNodeEnd(const QSvgMarker *a0)
  void visitMarkerNodeEnd(const QSvgMarker *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSvgVisitorCall30 call = reinterpret_cast<CuteQSvgVisitorCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitMarkerNodeEnd(a0);
  }

  //  bool QSvgVisitor::visitPatternNodeStart(const QSvgPattern *a0)
  bool visitPatternNodeStart(const QSvgPattern *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSvgVisitorCall31 call = reinterpret_cast<CuteQSvgVisitorCall31>(taken[31]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitPatternNodeStart(a0);
  }

  //  void QSvgVisitor::visitPatternNodeEnd(const QSvgPattern *a0)
  void visitPatternNodeEnd(const QSvgPattern *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSvgVisitorCall32 call = reinterpret_cast<CuteQSvgVisitorCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitPatternNodeEnd(a0);
  }

  //  bool QSvgVisitor::visitFilterNodeStart(const QSvgFilterContainer
  //      *node)
  bool visitFilterNodeStart(const QSvgFilterContainer *node) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSvgVisitorCall33 call = reinterpret_cast<CuteQSvgVisitorCall33>(taken[33]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitFilterNodeStart(node);
  }

  //  void QSvgVisitor::visitFilterNodeEnd(const QSvgFilterContainer *node)
  void visitFilterNodeEnd(const QSvgFilterContainer *node) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSvgVisitorCall34 call = reinterpret_cast<CuteQSvgVisitorCall34>(taken[34]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitFilterNodeEnd(node);
  }

  //  bool QSvgVisitor::visitFeFilterPrimitiveNodeStart(const
  //      QSvgFeFilterPrimitive *node)
  bool visitFeFilterPrimitiveNodeStart(
      const QSvgFeFilterPrimitive *node) override {
    if (taken[35]) {
      int handled = 0;
      CuteQSvgVisitorCall35 call = reinterpret_cast<CuteQSvgVisitorCall35>(taken[35]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QSvgVisitor::visitFeFilterPrimitiveNodeStart(node);
  }

  //  void QSvgVisitor::visitFeFilterPrimitiveNodeEnd(const
  //      QSvgFeFilterPrimitive *node)
  void visitFeFilterPrimitiveNodeEnd(
      const QSvgFeFilterPrimitive *node) override {
    if (taken[36]) {
      int handled = 0;
      CuteQSvgVisitorCall36 call = reinterpret_cast<CuteQSvgVisitorCall36>(taken[36]);
      call(this, node, &handled);
      if (handled) return;
    }
    QSvgVisitor::visitFeFilterPrimitiveNodeEnd(node);
  }
};

//  QSvgVisitor::QSvgVisitor()
extern "C" Q_DECL_EXPORT
QSvgVisitor *ritual_ZN11QSvgVisitorC1Ev() {
  return new CuteQSvgVisitor();
}

//  QSvgVisitor::~QSvgVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitorD1Ev(QSvgVisitor *self) {
  delete self;
}

//  void QSvgVisitor::traverse(const QSvgStructureNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor8traverseEPK17QSvgStructureNode(
    QSvgVisitor *self,
    const QSvgStructureNode *node) {
  self->traverse(node);
}

//  void QSvgVisitor::traverse(const QSvgNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor8traverseEPK8QSvgNode(
    QSvgVisitor *self,
    const QSvgNode *node) {
  self->traverse(node);
}

//  void QSvgVisitor::visitNode(const QSvgNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor9visitNodeEPK8QSvgNode(
    QSvgVisitor *self,
    const QSvgNode *a0) {
  self->visitNode(a0);
}

//  bool QSvgVisitor::visitStructureNodeStart(const QSvgStructureNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor23visitStructureNodeStartEPK17QSvgStructureNode(
    QSvgVisitor *self,
    const QSvgStructureNode *node) {
  return self->visitStructureNodeStart(node);
}

//  void QSvgVisitor::visitStructureNodeEnd(const QSvgStructureNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor21visitStructureNodeEndEPK17QSvgStructureNode(
    QSvgVisitor *self,
    const QSvgStructureNode *a0) {
  self->visitStructureNodeEnd(a0);
}

//  void QSvgVisitor::visitAnimateNode(const QSvgAnimateNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor16visitAnimateNodeEPK15QSvgAnimateNode(
    QSvgVisitor *self,
    const QSvgAnimateNode *node) {
  self->visitAnimateNode(node);
}

//  void QSvgVisitor::visitEllipseNode(const QSvgEllipse *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor16visitEllipseNodeEPK11QSvgEllipse(
    QSvgVisitor *self,
    const QSvgEllipse *node) {
  self->visitEllipseNode(node);
}

//  void QSvgVisitor::visitImageNode(const QSvgImage *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor14visitImageNodeEPK9QSvgImage(
    QSvgVisitor *self,
    const QSvgImage *node) {
  self->visitImageNode(node);
}

//  void QSvgVisitor::visitLineNode(const QSvgLine *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor13visitLineNodeEPK8QSvgLine(
    QSvgVisitor *self,
    const QSvgLine *node) {
  self->visitLineNode(node);
}

//  void QSvgVisitor::visitPathNode(const QSvgPath *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor13visitPathNodeEPK8QSvgPath(
    QSvgVisitor *self,
    const QSvgPath *node) {
  self->visitPathNode(node);
}

//  void QSvgVisitor::visitPolygonNode(const QSvgPolygon *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor16visitPolygonNodeEPK11QSvgPolygon(
    QSvgVisitor *self,
    const QSvgPolygon *node) {
  self->visitPolygonNode(node);
}

//  void QSvgVisitor::visitPolylineNode(const QSvgPolyline *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor17visitPolylineNodeEPK12QSvgPolyline(
    QSvgVisitor *self,
    const QSvgPolyline *node) {
  self->visitPolylineNode(node);
}

//  void QSvgVisitor::visitRectNode(const QSvgRect *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor13visitRectNodeEPK8QSvgRect(
    QSvgVisitor *self,
    const QSvgRect *node) {
  self->visitRectNode(node);
}

//  void QSvgVisitor::visitTextNode(const QSvgText *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor13visitTextNodeEPK8QSvgText(
    QSvgVisitor *self,
    const QSvgText *node) {
  self->visitTextNode(node);
}

//  void QSvgVisitor::visitTspanNode(const QSvgTspan *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor14visitTspanNodeEPK9QSvgTspan(
    QSvgVisitor *self,
    const QSvgTspan *node) {
  self->visitTspanNode(node);
}

//  void QSvgVisitor::visitUseNode(const QSvgUse *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor12visitUseNodeEPK7QSvgUse(
    QSvgVisitor *self,
    const QSvgUse *node) {
  self->visitUseNode(node);
}

//  void QSvgVisitor::visitVideoNode(const QSvgVideo *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor14visitVideoNodeEPK9QSvgVideo(
    QSvgVisitor *self,
    const QSvgVideo *node) {
  self->visitVideoNode(node);
}

//  bool QSvgVisitor::visitDocumentNodeStart(const QSvgDocument *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor22visitDocumentNodeStartEPK12QSvgDocument(
    QSvgVisitor *self,
    const QSvgDocument *node) {
  return self->visitDocumentNodeStart(node);
}

//  void QSvgVisitor::visitDocumentNodeEnd(const QSvgDocument *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor20visitDocumentNodeEndEPK12QSvgDocument(
    QSvgVisitor *self,
    const QSvgDocument *node) {
  self->visitDocumentNodeEnd(node);
}

//  bool QSvgVisitor::visitGroupNodeStart(const QSvgG *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor19visitGroupNodeStartEPK5QSvgG(
    QSvgVisitor *self,
    const QSvgG *node) {
  return self->visitGroupNodeStart(node);
}

//  void QSvgVisitor::visitGroupNodeEnd(const QSvgG *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor17visitGroupNodeEndEPK5QSvgG(
    QSvgVisitor *self,
    const QSvgG *node) {
  self->visitGroupNodeEnd(node);
}

//  bool QSvgVisitor::visitDefsNodeStart(const QSvgDefs *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor18visitDefsNodeStartEPK8QSvgDefs(
    QSvgVisitor *self,
    const QSvgDefs *node) {
  return self->visitDefsNodeStart(node);
}

//  void QSvgVisitor::visitDefsNodeEnd(const QSvgDefs *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor16visitDefsNodeEndEPK8QSvgDefs(
    QSvgVisitor *self,
    const QSvgDefs *node) {
  self->visitDefsNodeEnd(node);
}

//  bool QSvgVisitor::visitSwitchNodeStart(const QSvgSwitch *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor20visitSwitchNodeStartEPK10QSvgSwitch(
    QSvgVisitor *self,
    const QSvgSwitch *node) {
  return self->visitSwitchNodeStart(node);
}

//  void QSvgVisitor::visitSwitchNodeEnd(const QSvgSwitch *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor18visitSwitchNodeEndEPK10QSvgSwitch(
    QSvgVisitor *self,
    const QSvgSwitch *node) {
  self->visitSwitchNodeEnd(node);
}

//  bool QSvgVisitor::visitMaskNodeStart(const QSvgMask *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor18visitMaskNodeStartEPK8QSvgMask(
    QSvgVisitor *self,
    const QSvgMask *node) {
  return self->visitMaskNodeStart(node);
}

//  void QSvgVisitor::visitMaskNodeEnd(const QSvgMask *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor16visitMaskNodeEndEPK8QSvgMask(
    QSvgVisitor *self,
    const QSvgMask *node) {
  self->visitMaskNodeEnd(node);
}

//  bool QSvgVisitor::visitSymbolNodeStart(const QSvgSymbol *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor20visitSymbolNodeStartEPK10QSvgSymbol(
    QSvgVisitor *self,
    const QSvgSymbol *node) {
  return self->visitSymbolNodeStart(node);
}

//  void QSvgVisitor::visitSymbolNodeEnd(const QSvgSymbol *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor18visitSymbolNodeEndEPK10QSvgSymbol(
    QSvgVisitor *self,
    const QSvgSymbol *node) {
  self->visitSymbolNodeEnd(node);
}

//  bool QSvgVisitor::visitMarkerNodeStart(const QSvgMarker *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor20visitMarkerNodeStartEPK10QSvgMarker(
    QSvgVisitor *self,
    const QSvgMarker *a0) {
  return self->visitMarkerNodeStart(a0);
}

//  void QSvgVisitor::visitMarkerNodeEnd(const QSvgMarker *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor18visitMarkerNodeEndEPK10QSvgMarker(
    QSvgVisitor *self,
    const QSvgMarker *a0) {
  self->visitMarkerNodeEnd(a0);
}

//  bool QSvgVisitor::visitPatternNodeStart(const QSvgPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor21visitPatternNodeStartEPK11QSvgPattern(
    QSvgVisitor *self,
    const QSvgPattern *a0) {
  return self->visitPatternNodeStart(a0);
}

//  void QSvgVisitor::visitPatternNodeEnd(const QSvgPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor19visitPatternNodeEndEPK11QSvgPattern(
    QSvgVisitor *self,
    const QSvgPattern *a0) {
  self->visitPatternNodeEnd(a0);
}

//  bool QSvgVisitor::visitFilterNodeStart(const QSvgFilterContainer *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor20visitFilterNodeStartEPK19QSvgFilterContainer(
    QSvgVisitor *self,
    const QSvgFilterContainer *node) {
  return self->visitFilterNodeStart(node);
}

//  void QSvgVisitor::visitFilterNodeEnd(const QSvgFilterContainer *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor18visitFilterNodeEndEPK19QSvgFilterContainer(
    QSvgVisitor *self,
    const QSvgFilterContainer *node) {
  self->visitFilterNodeEnd(node);
}

//  bool QSvgVisitor::visitFeFilterPrimitiveNodeStart(const
//      QSvgFeFilterPrimitive *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSvgVisitor31visitFeFilterPrimitiveNodeStartEPK21QSvgFeFilterPrimitive(
    QSvgVisitor *self,
    const QSvgFeFilterPrimitive *node) {
  return self->visitFeFilterPrimitiveNodeStart(node);
}

//  void QSvgVisitor::visitFeFilterPrimitiveNodeEnd(const
//      QSvgFeFilterPrimitive *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgVisitor29visitFeFilterPrimitiveNodeEndEPK21QSvgFeFilterPrimitive(
    QSvgVisitor *self,
    const QSvgFeFilterPrimitive *node) {
  self->visitFeFilterPrimitiveNodeEnd(node);
}

//  a Python function taken by a CuteQSvgVisitor, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgVisitor(
    QSvgVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgVisitor *>(self)->take(key, call);
}

//  void QSvgVisitor::traverse(const QSvgStructureNode *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor8traverseEPK17QSvgStructureNode(
    QSvgVisitor *self,
    const QSvgStructureNode *node) {
  self->QSvgVisitor::traverse(node);
}

//  void QSvgVisitor::traverse(const QSvgNode *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor8traverseEPK8QSvgNode(
    QSvgVisitor *self,
    const QSvgNode *node) {
  self->QSvgVisitor::traverse(node);
}

//  void QSvgVisitor::visitNode(const QSvgNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor9visitNodeEPK8QSvgNode(
    QSvgVisitor *self,
    const QSvgNode *a0) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitNode(a0);
}

//  bool QSvgVisitor::visitStructureNodeStart(const QSvgStructureNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor23visitStructureNodeStartEPK17QSvgStructureNode(
    QSvgVisitor *self,
    const QSvgStructureNode *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitStructureNodeStart(
      node);
}

//  void QSvgVisitor::visitStructureNodeEnd(const QSvgStructureNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor21visitStructureNodeEndEPK17QSvgStructureNode(
    QSvgVisitor *self,
    const QSvgStructureNode *a0) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitStructureNodeEnd(
      a0);
}

//  void QSvgVisitor::visitAnimateNode(const QSvgAnimateNode *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor16visitAnimateNodeEPK15QSvgAnimateNode(
    QSvgVisitor *self,
    const QSvgAnimateNode *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitAnimateNode(
      node);
}

//  void QSvgVisitor::visitEllipseNode(const QSvgEllipse *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor16visitEllipseNodeEPK11QSvgEllipse(
    QSvgVisitor *self,
    const QSvgEllipse *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitEllipseNode(
      node);
}

//  void QSvgVisitor::visitImageNode(const QSvgImage *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor14visitImageNodeEPK9QSvgImage(
    QSvgVisitor *self,
    const QSvgImage *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitImageNode(node);
}

//  void QSvgVisitor::visitLineNode(const QSvgLine *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor13visitLineNodeEPK8QSvgLine(
    QSvgVisitor *self,
    const QSvgLine *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitLineNode(node);
}

//  void QSvgVisitor::visitPathNode(const QSvgPath *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor13visitPathNodeEPK8QSvgPath(
    QSvgVisitor *self,
    const QSvgPath *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitPathNode(node);
}

//  void QSvgVisitor::visitPolygonNode(const QSvgPolygon *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor16visitPolygonNodeEPK11QSvgPolygon(
    QSvgVisitor *self,
    const QSvgPolygon *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitPolygonNode(
      node);
}

//  void QSvgVisitor::visitPolylineNode(const QSvgPolyline *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor17visitPolylineNodeEPK12QSvgPolyline(
    QSvgVisitor *self,
    const QSvgPolyline *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitPolylineNode(
      node);
}

//  void QSvgVisitor::visitRectNode(const QSvgRect *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor13visitRectNodeEPK8QSvgRect(
    QSvgVisitor *self,
    const QSvgRect *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitRectNode(node);
}

//  void QSvgVisitor::visitTextNode(const QSvgText *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor13visitTextNodeEPK8QSvgText(
    QSvgVisitor *self,
    const QSvgText *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitTextNode(node);
}

//  void QSvgVisitor::visitTspanNode(const QSvgTspan *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor14visitTspanNodeEPK9QSvgTspan(
    QSvgVisitor *self,
    const QSvgTspan *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitTspanNode(node);
}

//  void QSvgVisitor::visitUseNode(const QSvgUse *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor12visitUseNodeEPK7QSvgUse(
    QSvgVisitor *self,
    const QSvgUse *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitUseNode(node);
}

//  void QSvgVisitor::visitVideoNode(const QSvgVideo *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor14visitVideoNodeEPK9QSvgVideo(
    QSvgVisitor *self,
    const QSvgVideo *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitVideoNode(node);
}

//  bool QSvgVisitor::visitDocumentNodeStart(const QSvgDocument *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor22visitDocumentNodeStartEPK12QSvgDocument(
    QSvgVisitor *self,
    const QSvgDocument *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitDocumentNodeStart(
      node);
}

//  void QSvgVisitor::visitDocumentNodeEnd(const QSvgDocument *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor20visitDocumentNodeEndEPK12QSvgDocument(
    QSvgVisitor *self,
    const QSvgDocument *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitDocumentNodeEnd(
      node);
}

//  bool QSvgVisitor::visitGroupNodeStart(const QSvgG *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor19visitGroupNodeStartEPK5QSvgG(
    QSvgVisitor *self,
    const QSvgG *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitGroupNodeStart(
      node);
}

//  void QSvgVisitor::visitGroupNodeEnd(const QSvgG *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor17visitGroupNodeEndEPK5QSvgG(
    QSvgVisitor *self,
    const QSvgG *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitGroupNodeEnd(
      node);
}

//  bool QSvgVisitor::visitDefsNodeStart(const QSvgDefs *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor18visitDefsNodeStartEPK8QSvgDefs(
    QSvgVisitor *self,
    const QSvgDefs *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitDefsNodeStart(
      node);
}

//  void QSvgVisitor::visitDefsNodeEnd(const QSvgDefs *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor16visitDefsNodeEndEPK8QSvgDefs(
    QSvgVisitor *self,
    const QSvgDefs *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitDefsNodeEnd(
      node);
}

//  bool QSvgVisitor::visitSwitchNodeStart(const QSvgSwitch *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor20visitSwitchNodeStartEPK10QSvgSwitch(
    QSvgVisitor *self,
    const QSvgSwitch *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitSwitchNodeStart(
      node);
}

//  void QSvgVisitor::visitSwitchNodeEnd(const QSvgSwitch *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor18visitSwitchNodeEndEPK10QSvgSwitch(
    QSvgVisitor *self,
    const QSvgSwitch *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitSwitchNodeEnd(
      node);
}

//  bool QSvgVisitor::visitMaskNodeStart(const QSvgMask *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor18visitMaskNodeStartEPK8QSvgMask(
    QSvgVisitor *self,
    const QSvgMask *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitMaskNodeStart(
      node);
}

//  void QSvgVisitor::visitMaskNodeEnd(const QSvgMask *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor16visitMaskNodeEndEPK8QSvgMask(
    QSvgVisitor *self,
    const QSvgMask *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitMaskNodeEnd(
      node);
}

//  bool QSvgVisitor::visitSymbolNodeStart(const QSvgSymbol *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor20visitSymbolNodeStartEPK10QSvgSymbol(
    QSvgVisitor *self,
    const QSvgSymbol *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitSymbolNodeStart(
      node);
}

//  void QSvgVisitor::visitSymbolNodeEnd(const QSvgSymbol *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor18visitSymbolNodeEndEPK10QSvgSymbol(
    QSvgVisitor *self,
    const QSvgSymbol *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitSymbolNodeEnd(
      node);
}

//  bool QSvgVisitor::visitMarkerNodeStart(const QSvgMarker *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor20visitMarkerNodeStartEPK10QSvgMarker(
    QSvgVisitor *self,
    const QSvgMarker *a0) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitMarkerNodeStart(
      a0);
}

//  void QSvgVisitor::visitMarkerNodeEnd(const QSvgMarker *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor18visitMarkerNodeEndEPK10QSvgMarker(
    QSvgVisitor *self,
    const QSvgMarker *a0) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitMarkerNodeEnd(
      a0);
}

//  bool QSvgVisitor::visitPatternNodeStart(const QSvgPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor21visitPatternNodeStartEPK11QSvgPattern(
    QSvgVisitor *self,
    const QSvgPattern *a0) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitPatternNodeStart(
      a0);
}

//  void QSvgVisitor::visitPatternNodeEnd(const QSvgPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor19visitPatternNodeEndEPK11QSvgPattern(
    QSvgVisitor *self,
    const QSvgPattern *a0) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitPatternNodeEnd(
      a0);
}

//  bool QSvgVisitor::visitFilterNodeStart(const QSvgFilterContainer *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor20visitFilterNodeStartEPK19QSvgFilterContainer(
    QSvgVisitor *self,
    const QSvgFilterContainer *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitFilterNodeStart(
      node);
}

//  void QSvgVisitor::visitFilterNodeEnd(const QSvgFilterContainer *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor18visitFilterNodeEndEPK19QSvgFilterContainer(
    QSvgVisitor *self,
    const QSvgFilterContainer *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitFilterNodeEnd(
      node);
}

//  bool QSvgVisitor::visitFeFilterPrimitiveNodeStart(const
//      QSvgFeFilterPrimitive *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSvgVisitor31visitFeFilterPrimitiveNodeStartEPK21QSvgFeFilterPrimitive(
    QSvgVisitor *self,
    const QSvgFeFilterPrimitive *node) {
  return static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitFeFilterPrimitiveNodeStart(
      node);
}

//  void QSvgVisitor::visitFeFilterPrimitiveNodeEnd(const
//      QSvgFeFilterPrimitive *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSvgVisitor29visitFeFilterPrimitiveNodeEndEPK21QSvgFeFilterPrimitive(
    QSvgVisitor *self,
    const QSvgFeFilterPrimitive *node) {
  static_cast<OwnQSvgVisitor *>(self)->OwnQSvgVisitor::visitFeFilterPrimitiveNodeEnd(
      node);
}
